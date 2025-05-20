import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# LLM Service Configuration
LLM_SERVICE = os.getenv("LLM_SERVICE", "ollama")
MODEL = os.getenv("MODEL", "deepseek-r1:32b")

# Embedding Service Configuration
EMBEDDING_SERVICE = os.getenv("EMBEDDING_SERVICE", "openai")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")

# Ollama Configuration
OLLAMA_SERVER = os.getenv("OLLAMA_SERVER", "http://localhost:11434")
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# App Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
APP_PORT = int(os.getenv("APP_PORT", 5014))

# Data paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app", "data")
VECTOR_STORE_PATH = os.path.join(DATA_DIR, "vector_store")

# Ensure necessary directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(VECTOR_STORE_PATH, exist_ok=True) 