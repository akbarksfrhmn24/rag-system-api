# app/query.py
from app.vector_store import get_vector_store
from app.llm_service import query_ollama  # Now using the CLI-based function
from app.embedding import LocalEmbedding  # Your local embedding class

def answer_query(question: str, k: int = 4) -> dict:
    # Retrieve the vector store
    vector_store = get_vector_store()
    
    # Instantiate the local embedding model
    embedding_model = LocalEmbedding()
    
    # Generate the query embedding using the local embedding model
    question_embedding = embedding_model.embed_query(question)
    
    # Perform a similarity search using the query embedding
    results = vector_store.similarity_search_by_vector(question_embedding, k=k)
    
    # Build context and citations from the retrieved document chunks
    context = ""
    citations = []
    for i, doc in enumerate(results):
        context += f"Context {i+1}: {doc.page_content}\n"
        citations.append(doc.metadata.get("source", "unknown"))
    
    # Construct the prompt for generation
    prompt = (
        f"Answer the following question based on the provided context:\n\n"
        f"Context:\n{context}\n"
        f"Question: {question}\n"
        f"Answer:"
    )
    
    # Generate an answer using the local Ollama CLI call
    answer = query_ollama(prompt)
    
    return {"answer": answer, "citations": citations}
