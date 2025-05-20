from langchain_community.embeddings import OllamaEmbeddings
from typing import List, Dict, Any, Optional
import os
from app.config import (
    EMBEDDING_SERVICE,
    EMBEDDING_MODEL,
    OLLAMA_SERVER
)

class EmbeddingProvider:
    """
    Provides embedding functionality with support for Ollama embeddings.
    """
    
    def __init__(self):
        """
        Initialize the embedding provider based on configuration.
        """
        self.embedding_model = self._initialize_embedding_model()
    
    def _initialize_embedding_model(self):
        """
        Initialize the Ollama embedding model based on configuration.
        
        Returns:
            An initialized embedding model instance
        """
        if EMBEDDING_SERVICE.lower() == "ollama":
            return OllamaEmbeddings(
                model=EMBEDDING_MODEL,
                base_url=OLLAMA_SERVER
            )
        
        else:
            raise ValueError(f"Unsupported embedding service: {EMBEDDING_SERVICE}. Currently only 'ollama' is supported.")
    
    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Get embeddings for a list of texts.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        return self.embedding_model.embed_documents(texts)
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Get embedding for a single text string.
        
        Args:
            text: Text string to embed
            
        Returns:
            Embedding vector
        """
        return self.embedding_model.embed_query(text) 