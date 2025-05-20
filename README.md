# NUST Bank AI Assistant

A Large Language Model (LLM)-based solution for enhancing customer service in a banking environment.

## Project Overview

This project implements an AI-driven assistant for a local bank (NUST Bank) that can handle customer inquiries about banking services, account information, and policies. It uses Retrieval-Augmented Generation (RAG) with local LLM integration to provide accurate and context-aware responses.

### Core Features

1. **Data Ingestion & Preprocessing**: Automatic processing of JSON and Excel documents containing bank information.
2. **Large Language Model Integration**: Uses Ollama to run local LLMs for response generation.
3. **Embedding & Indexing**: Creates vector embeddings for efficient retrieval of relevant banking information.
4. **Guard Rails**: Implements safety measures to prevent inappropriate queries and limit responses to banking domains.
5. **User Interface**: Provides a clean, simple web interface for customer interactions.
6. **Real-Time Updates**: Supports adding new banking information through file uploads or manual document entry.

## Architecture

The system follows a Retrieval-Augmented Generation (RAG) architecture:

1. User queries are processed for safety and relevance
2. Relevant documents are retrieved from the vector store based on semantic similarity
3. Retrieved documents and the user query are processed by the LLM
4. The LLM generates a contextually appropriate response
5. Response is filtered to ensure no sensitive information is revealed

## Technical Details

- **Backend**: Flask web server with Python
- **LLM Service**: Ollama (default model: deepseek-r1:32b)
- **Embedding**: OpenAI or Ollama embedding models
- **Vector Store**: FAISS for similarity search
- **Frontend**: HTML/CSS/JavaScript with Bootstrap 5

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Ollama server running locally or remotely
- Redis server (optional, for production use)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd nust-bank-ai-assistant
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in `.env` file:
   ```
   LLM_SERVICE=ollama
   MODEL=deepseek-r1:32b
   EMBEDDING_SERVICE=openai
   EMBEDDING_MODEL=text-embedding-ada-002
   OLLAMA_SERVER=http://localhost:11434
   OPENAI_API_KEY=your_openai_key_here  # Only needed if using OpenAI embeddings
   ```

4. Run the application:
   ```
   python main.py
   ```

5. Access the web interface at `http://localhost:5014`

## Usage

1. **Ask Questions**: Type banking-related questions in the chat interface
2. **Upload Data**: Add new banking documents through the upload interface
3. **Add Documents**: Manually add Q&A pairs through the document interface

## Project Status

This is a prototype implementation for the CS416: Large Language Models class project.

## Acknowledgments

- CS416: Large Language Models course instructors and TAs
- NUST for providing the project requirements

## License

This project is for educational purposes only. 