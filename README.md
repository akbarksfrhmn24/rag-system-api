# RAG System API

A Retrieval-Augmented Generation (RAG) system for technical documentation that ingests documents (PDF/Markdown), processes them into embeddings using SentenceTransformers, stores them in a persistent Chroma vector store, and answers queries using a local LLM via Ollama CLI.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [Testing the API](#testing-the-api)
- [Future Improvements](#future-improvements)

## Features
- **Document Ingestion:** Upload PDF or Markdown files to extract text and generate embeddings.
- **Vector Store:** Use ChromaDB to store document embeddings persistently.
- **Local Embeddings:** Generate embeddings with SentenceTransformers.
- **Local Generation:** Generate answers via a locally installed Ollama CLI.
- **API Monitoring:** Basic metrics tracking for token usage, response times, and success/failure counts.
- **Interactive Documentation:** Swagger UI available for testing endpoints.

## Technology Stack
- **Python 3.11**
- **FastAPI** for building the API.
- **LangChain** for RAG integration.
- **ChromaDB** as the vector store.
- **Sentence-Transformers** for local embedding generation.
- **Ollama CLI** for local LLM text generation.
- **Docker** and **Docker Compose** for containerization.

## Installation

### Clone the Repository
```bash
git clone https://github.com/akbarksfrhmn24/rag-system-api.git
cd rag-system-api
```
### Install Python Dependencies
To install locally, run:
```bash
pip install -r requirements.txt
```

## Usaage

### Running Locally
You can start the FastAPI server with:
```bash
uvicorn app.main:app --reload
```
or
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
The API will be available at http://localhost:8000.

### Runnning With Docker
From the project root, build and run the containers with:
```bash
docker compose up --build
```
or you can run
```bash
docker compose up -d
```
to running on the background

### API Endpoints
## Upload Document
  Endpoint: POST /upload
  Description: Upload a PDF or Markdown file to ingest into the system.
  Request: Multipart form-data with a key file.
  Example cURL:
```bash
curl -X POST -F "file=@/path/to/your/document.pdf" http://localhost:8000/upload
```
### Query Documents
  Endpoint: POST /query
  Description: Query the ingested documents by sending a JSON body with a question.
  Request Body Example:
```json
{
  "question": "How do I install the software?"
}
```
Example cURL:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"question": "How do I install the software?"}' \
     http://localhost:8000/query
```
### Get Metrics
  Endpoint: GET /metrics
  Description: Retrieve system metrics such as token usage, response times, and success/failure counts.
  Example cURL:
```bash
curl http://localhost:8000/metrics
```
## Interactive Documentation
1. Access Swagger UI at: http://localhost:8000/docs
2. Alternatively, view ReDoc at: http://localhost:8000/redoc

## Testing the API
Use Postman or any API client to:
1. Upload a document via the /upload endpoint.
2. Query the system with a JSON request to the /query endpoint.
3. Retrieve metrics with the /metrics endpoint.
You can also use the interactive Swagger UI at /docs to explore and test the API.
## Future Improvements
1. Advanced Error Handling: Enhance error logging and handling throughout the API.
2. Authentication: Add security measures such as API keys or OAuth.
3. Enhanced Preprocessing: Improve document processing and chunking.
4. Caching: Implement caching to optimize performance.
5. Model Flexibility: Allow switching between different embedding or LLM generation models.
