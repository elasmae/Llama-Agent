
#  LlamaIndex Agent Project

A complete LLMOps project built with **LlamaIndex** and **OpenAI**.

Includes: Basic, Tool-Augmented, Stateful, Multi-Agent systems + FastAPI, Gradio UI, RAG with ChromaDB.


##  What’s Included

- Multilingual LLM agents (basic, tool-based, stateful, multi-agent)
- FastAPI backend + Gradio interface
- RAG agent using ChromaDB vector search
- Docker & Docker Compose support
- Terraform infrastructure (GCP-ready)
- CI/CD pipeline with GitHub Actions:
  - Pytest for unit tests
  - Black for formatting
  - Flake8 for linting
  - Docker build verification
- Makefile for simplified DevOps commands


## 📦 MLOps Highlights

- Testable agent pipelines with `pytest`
- Consistent code quality: `black`, `flake8`
- Reproducible environments with Docker
- CI/CD integration with GitHub Actions
- Retrieval-augmented agents with ChromaDB


## 📁  Structure

```
agents/       → Agent definitions  
tools/        → Utility functions (math, etc.)  
retrieval/    → RAG agent logic  
vector_db/    → ChromaDB vector DB integration  
app/          → FastAPI backend  
gradio_ui/    → Gradio web UI  
tests/        → Unit tests  
```

