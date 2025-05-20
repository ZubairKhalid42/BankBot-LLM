# NUST Bank AI Assistant: System Architecture

## Overview

The NUST Bank AI Assistant is designed with a Retrieval-Augmented Generation (RAG) architecture that combines document retrieval with language model generation to provide accurate and contextual responses to banking queries.

## Architecture Diagram

```
┌───────────────────────────────────────────────────────────────────────┐
│                        NUST Bank AI Assistant                          │
└───────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────────────┐
│                            Flask Web Server                            │
└───────────────────────────────────────────────────────────────────────┘
                                    │
                 ┌─────────────────┬┴┬─────────────────┐
                 │                 │ │                 │
                 ▼                 ▼ │                 ▼
┌───────────────────────┐ ┌──────────────────┐ ┌───────────────────────┐
│     User Interface    │ │ Document Upload  │ │    Document Input     │
│   (HTML/CSS/JS/AJAX)  │ │    Interface     │ │      Interface        │
└───────────────────────┘ └──────────────────┘ └───────────────────────┘
                 │                 │                     │
                 └─────────────────┼─────────────────────┘
                                   │
                                   ▼
┌───────────────────────────────────────────────────────────────────────┐
│                        RAG Model Application                           │
└───────────────────────────────────────────────────────────────────────┘
                                   │
           ┌─────────────────────┬─┴─┬─────────────────────┐
           │                     │   │                     │
           ▼                     ▼   │                     ▼
┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────────┐
│  Query Processing   │ │ Document Retrieval  │ │   Data Processing   │
│   & Guard Rails     │ │  & Vector Store     │ │    & Ingestion      │
└─────────────────────┘ └─────────────────────┘ └─────────────────────┘
           │                     │                     │
           │                     │                     │
           │                     ▼                     │
           │         ┌─────────────────────┐          │
           │         │  Embedding Service  │          │
           │         │  (OpenAI/Ollama)    │          │
           │         └─────────────────────┘          │
           │                     │                     │
           └─────────────────────┼─────────────────────┘
                                 │
                                 ▼
                     ┌─────────────────────┐
                     │    LLM Provider     │
                     │  (Ollama/OpenAI)    │
                     └─────────────────────┘
```

## Component Description

1. **Flask Web Server**: Provides the HTTP interface for the application, handling user requests and serving the web UI.

2. **User Interface**: Web-based chat interface allowing users to interact with the AI assistant.

3. **Document Upload/Input Interfaces**: Allow administrators to add new banking knowledge to the system.

4. **RAG Model Application**: Core component that orchestrates the entire process:
   - **Query Processing & Guard Rails**: Validates user queries and prevents harmful or out-of-domain requests.
   - **Document Retrieval & Vector Store**: Manages the vector database and retrieves relevant documents.
   - **Data Processing & Ingestion**: Handles processing and sanitization of banking knowledge.

5. **Embedding Service**: Generates vector embeddings for documents and queries, using either OpenAI or Ollama embedding models.

6. **LLM Provider**: Generates human-like responses based on retrieved documents and user queries using Ollama (or OpenAI).

## Data Flow

1. User submits a query through the web interface.
2. Query is validated for safety and relevance.
3. The query is embedded using the embedding service.
4. Relevant documents are retrieved from the vector store using semantic similarity.
5. Retrieved documents and the query are sent to the LLM.
6. The LLM generates a contextual response.
7. Response is filtered and presented to the user.

## Technical Implementation

- **Backend**: Python with Flask
- **Vector Database**: FAISS 
- **LLM Integration**: Langchain for Ollama integration
- **Frontend**: Bootstrap 5 with JavaScript
- **Data Storage**: Local file system for vector store 