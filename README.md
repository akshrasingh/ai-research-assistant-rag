# AI Research Assistant (RAG System)

An AI-powered Research Assistant built using Retrieval-Augmented Generation (RAG) architecture.  
The system ingests multiple PDF documents, performs semantic search using FAISS vector embeddings, rewrites user queries for improved retrieval, and generates grounded answers using Ollama + Llama3.

---

# Features

- Multi-document Question Answering
- Semantic Search using FAISS
- Query Rewriting using LLM
- Metadata-aware Retrieval
- Source Attribution
- FastAPI Backend
- Local LLM Inference using Ollama
- Modular RAG Architecture

---

# Tech Stack

## Backend
- Python
- FastAPI

## AI / NLP
- Sentence Transformers
- Ollama
- Llama3

## Vector Database
- FAISS

## PDF Processing
- PyPDF

---

# Architecture

```text
Multiple PDFs
      ↓
Ingestion Pipeline
      ↓
Chunking + Metadata
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
User Query
      ↓
Query Rewriter
      ↓
Retriever
      ↓
Relevant Chunks
      ↓
Generator
      ↓
Ollama (Llama3)
      ↓
Final Answer
