import os


CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 512))

VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./data/chroma_db")

OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')