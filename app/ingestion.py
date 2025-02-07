# app/ingestion.py
import os
from pathlib import Path
import fitz  # PyMuPDF for PDF processing
from langchain.text_splitter import CharacterTextSplitter
from app.vector_store import get_vector_store
from app.embedding import LocalEmbedding

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_markdown(file_path: str) -> str:
    """Extract text from a Markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def process_document(file_path: str) -> list[str]:
    """Process the document based on its file extension and split it into chunks."""
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".md", ".markdown"]:
        text = extract_text_from_markdown(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    # Create a text splitter with a specified chunk size and overlap.
    splitter = CharacterTextSplitter(separator="\n", chunk_size=512, chunk_overlap=50)
    chunks = splitter.split_text(text)
    # Filter out any empty chunks.
    return [chunk for chunk in chunks if chunk.strip()]

def ingest_document(file_path: str):
    """
    Ingest a document by:
      1. Extracting text and splitting it into chunks.
      2. Generating embeddings for each chunk using LocalEmbedding.
      3. Adding the chunks along with their embeddings to the vector store.
    """
    # Process the document to get text chunks.
    chunks = process_document(file_path)
    
    if not chunks:
        raise ValueError("No valid text chunks found in the document.")

    # Instantiate the local embedding model.
    embedding_model = LocalEmbedding()
    # Retrieve the persistent vector store (Chroma).
    vector_store = get_vector_store()

    # Process each text chunk.
    for chunk in chunks:
        try:
            # Generate an embedding for the chunk.
            embedding = embedding_model.embed_query(chunk)
        except Exception as e:
            raise ValueError(f"Failed to get embedding for chunk: {chunk[:30]}... Error: {e}")

        if not embedding or len(embedding) == 0:
            raise ValueError(f"Empty embedding returned for chunk: {chunk[:30]}...")

        # Debug: Print embedding details.
        print(f"Chunk: {chunk[:30]}... | Embedding length: {len(embedding)} | First 3 values: {embedding[:3]}")

        # Add the text chunk along with its embedding and source metadata to the vector store.
        vector_store.add_texts(
            texts=[chunk],
            metadatas=[{"source": os.path.basename(file_path)}],
            embeddings=[embedding]
        )
    
    # Persist the vector store.
    vector_store.persist()
