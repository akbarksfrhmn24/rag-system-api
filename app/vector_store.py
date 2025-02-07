# app/vector_store.py
import os
from langchain_community.vectorstores import Chroma
from app.embedding import LocalEmbedding
from app.config import VECTOR_STORE_PATH

def get_vector_store() -> Chroma:
    """
    Load an existing Chroma vector store from the persistence directory or create a new one.
    Uses the LocalEmbedding class to generate embeddings.
    """
    # Instantiate the local embedding model.
    embedding_model = LocalEmbedding()
    persist_directory = VECTOR_STORE_PATH

    if os.path.exists(persist_directory) and os.listdir(persist_directory):
        # If the persistence directory exists and is not empty,
        # load the existing Chroma vector store.
        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model  # Pass the embedding instance.
        )
    else:
        # Create a new Chroma vector store (collection) with no texts initially.
        vector_store = Chroma.from_texts(
            texts=[],  # Start with an empty collection.
            embedding=embedding_model,  # Use the LocalEmbedding instance.
            persist_directory=persist_directory,
            collection_name="documents"
        )
    return vector_store
