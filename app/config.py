import os

# size for chunking
CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 512))

# location of chromadb or vector store
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./data/chroma_db")

# location of the model
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')