import os
import pickle
from typing import List, Dict, Any, Optional
from langchain_community.vectorstores import FAISS
from langchain.schema.document import Document
from app.utils.embeddings import EmbeddingProvider
from app.config import VECTOR_STORE_PATH

class VectorStore:
    """
    Manages the vector store for document retrieval.
    """
    
    def __init__(self):
        """
        Initialize the vector store with the embedding provider.
        """
        self.embedding_provider = EmbeddingProvider()
        self.vector_store = None
        self.vector_store_path = os.path.join(VECTOR_STORE_PATH, "faiss_index")
    
    def _convert_to_documents(self, items: List[Dict[str, Any]]) -> List[Document]:
        """
        Convert dictionary items to Document objects for the vector store.
        
        Args:
            items: List of dictionary items to convert
            
        Returns:
            List of Document objects
        """
        documents = []
        
        for item in items:
            # Extract the text content
            content = item.get('content', '')
            
            # Create metadata from the rest of the fields
            metadata = {k: v for k, v in item.items() if k != 'content'}
            
            # Create a Document
            document = Document(
                page_content=content,
                metadata=metadata
            )
            
            documents.append(document)
        
        return documents
    
    def create_vector_store(self, items: List[Dict[str, Any]]) -> None:
        """
        Create a new vector store from the provided items.
        
        Args:
            items: List of dictionary items to add to the vector store
        """
        documents = self._convert_to_documents(items)
        
        # Create the vector store
        self.vector_store = FAISS.from_documents(
            documents,
            self.embedding_provider.embedding_model
        )
        
        # Save the vector store
        self.save_vector_store()
    
    def add_to_vector_store(self, items: List[Dict[str, Any]]) -> None:
        """
        Add items to an existing vector store.
        
        Args:
            items: List of dictionary items to add to the vector store
        """
        if self.vector_store is None:
            # If no vector store exists, create a new one
            return self.create_vector_store(items)
        
        documents = self._convert_to_documents(items)
        
        # Add documents to the vector store
        self.vector_store.add_documents(documents)
        
        # Save the updated vector store
        self.save_vector_store()
    
    def save_vector_store(self) -> None:
        """
        Save the vector store to disk.
        """
        if self.vector_store is None:
            print("No vector store to save.")
            return
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.vector_store_path), exist_ok=True)
        
        # Save the FAISS index
        self.vector_store.save_local(self.vector_store_path)
        
        print(f"Vector store saved to {self.vector_store_path}")
    
    def load_vector_store(self) -> bool:
        """
        Load the vector store from disk.
        
        Returns:
            True if the vector store was loaded successfully, False otherwise
        """
        try:
            if os.path.exists(self.vector_store_path):
                # Load the FAISS index
                self.vector_store = FAISS.load_local(
                    self.vector_store_path,
                    self.embedding_provider.embedding_model
                )
                print(f"Vector store loaded from {self.vector_store_path}")
                return True
            else:
                print(f"Vector store file not found at {self.vector_store_path}")
                return False
        
        except Exception as e:
            print(f"Error loading vector store: {e}")
            return False
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """
        Perform a similarity search against the vector store.
        
        Args:
            query: Query string
            k: Number of results to return
            
        Returns:
            List of Document objects
        """
        if self.vector_store is None:
            print("No vector store loaded. Please create or load a vector store first.")
            return []
        
        return self.vector_store.similarity_search(query, k=k)
    
    def similarity_search_with_score(self, query: str, k: int = 4) -> List[tuple]:
        """
        Perform a similarity search against the vector store and return scores.
        
        Args:
            query: Query string
            k: Number of results to return
            
        Returns:
            List of (Document, score) tuples
        """
        if self.vector_store is None:
            print("No vector store loaded. Please create or load a vector store first.")
            return []
        
        return self.vector_store.similarity_search_with_score(query, k=k) 