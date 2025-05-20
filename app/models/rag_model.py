from typing import Dict, List, Any, Optional
from app.utils.vector_store import VectorStore
from app.utils.llm_provider import LLMProvider
from app.utils.data_processor import DataProcessor
from app.config import DATA_DIR
import os

class RAGModel:
    """
    Retrieval-Augmented Generation model that combines vector retrieval and LLM generation.
    """
    
    def __init__(self):
        """
        Initialize the RAG model with required components.
        """
        self.vector_store = VectorStore()
        self.llm_provider = LLMProvider()
        self.rag_chain = self.llm_provider.create_rag_chain()
        self.load_or_create_vector_store()
    
    def load_or_create_vector_store(self) -> None:
        """
        Load an existing vector store or create a new one if none exists.
        """
        # Try to load the vector store
        loaded = self.vector_store.load_vector_store()
        
        # If loading fails, create a new vector store from data
        if not loaded:
            print("Creating new vector store...")
            data_processor = DataProcessor(DATA_DIR)
            documents = data_processor.process_all_data()
            
            if documents:
                self.vector_store.create_vector_store(documents)
                print(f"Created vector store with {len(documents)} documents")
            else:
                print("No documents found to create vector store")
    
    def add_document(self, document: Dict[str, Any]) -> None:
        """
        Add a new document to the vector store.
        
        Args:
            document: Dictionary containing document information
        """
        # Add the document to the vector store
        self.vector_store.add_to_vector_store([document])
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user query and generate a response.
        
        Args:
            query: User's query string
            
        Returns:
            Dictionary containing response and related information
        """
        # Check for jailbreak attempts
        if self.llm_provider.handle_jailbreaking(query):
            response = (
                "I cannot process this request as it appears to be attempting to bypass "
                "my operational guidelines. Please submit a valid banking inquiry."
            )
            return {
                "response": response,
                "sources": [],
                "is_jailbreak": True,
                "is_out_of_domain": False
            }
        
        # Check if query is out of domain
        if self.llm_provider.is_out_of_domain(query):
            response = self.llm_provider.handle_out_of_domain_query(query)
            return {
                "response": response,
                "sources": [],
                "is_jailbreak": False,
                "is_out_of_domain": True
            }
        
        # Get relevant documents from vector store
        docs = self.vector_store.similarity_search(query, k=3)
        
        # Track sources for attribution
        sources = []
        for doc in docs:
            if 'source' in doc.metadata:
                source = doc.metadata['source']
                if source not in sources:
                    sources.append(source)
        
        # If no relevant documents found
        if not docs:
            response = (
                "I don't have enough information to answer this question. "
                "Please contact our customer service at +92 (51) 111 000 494 for assistance."
            )
        else:
            # Format documents for the prompt
            context = self.llm_provider.format_docs(docs)
            
            # Generate response using RAG chain
            response = self.rag_chain.invoke({
                "context": context,
                "question": query
            })
            
            # Apply content filtering
            response = self.llm_provider.apply_content_filtering(response)
        
        return {
            "response": response,
            "sources": sources,
            "is_jailbreak": False,
            "is_out_of_domain": False
        }
    
    def add_new_data(self, filepath: str) -> Dict[str, Any]:
        """
        Process and add new data from a file.
        
        Args:
            filepath: Path to the file to process
            
        Returns:
            Dictionary with status information
        """
        try:
            # Check if file exists
            if not os.path.exists(filepath):
                return {
                    "success": False,
                    "message": f"File not found: {filepath}"
                }
            
            # Create data processor
            data_processor = DataProcessor("")
            
            # Process file based on extension
            if filepath.lower().endswith('.json'):
                documents = data_processor.load_json_data(filepath)
            elif filepath.lower().endswith(('.xlsx', '.xls')):
                documents = data_processor.load_excel_data(filepath)
            else:
                return {
                    "success": False,
                    "message": f"Unsupported file format: {filepath}"
                }
            
            # Check if any documents were extracted
            if not documents:
                return {
                    "success": False,
                    "message": f"No valid data found in file: {filepath}"
                }
            
            # Add documents to vector store
            self.vector_store.add_to_vector_store(documents)
            
            return {
                "success": True,
                "message": f"Successfully added {len(documents)} documents from {filepath}",
                "document_count": len(documents)
            }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"Error processing file: {str(e)}"
            } 