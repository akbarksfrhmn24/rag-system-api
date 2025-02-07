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
git clone https://github.com/yourusername/rag-system-api.git
cd rag-system-api
