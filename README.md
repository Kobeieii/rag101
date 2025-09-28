# Simple RAG Example

This repository is for learning how to build a **Retrieval-Augmented Generation (RAG)** system using:

- [LangChain](https://www.langchain.com/) – framework for orchestration  
- [Hugging Face](https://huggingface.co/) – embeddings (`BAAI/bge-m3`)  
- [pgvector](https://github.com/pgvector/pgvector) – PostgreSQL vector store  
- [Ollama](https://ollama.ai/) or [OpenAI](https://openai.com/) – LLMs for answering queries  
- [uv](https://github.com/astral-sh/uv) – fast Python package manager  

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/Kobeieii/rag101.git
cd rag101
```

### 2. Install dependencies (with uv)
```bash
uv venv
uv pip install -r requirements.txt
```

### 3. Setup PostgreSQL with pgvector
```bash
docker compose up -d
```
This will start PostgreSQL with the `pgvector` extension, and automatically create a `documents` table.

### 4. Start Ollama (if using locally)
You can choose and pull any model listed on the [Ollama models page](https://ollama.ai/library).
```bash
ollama pull llama3.2
```

### 5. Run
```bash
uv run main.py
```
Example output 🥳
```text
2025-09-28 12:31:43,932 - INFO - Response: Thitiworada Khumpeng is a full-stack developer based in Bang Plee, Samutprakarn.
She holds a B.Eng. in Biomedical Engineering from Srinakarinwirot University (2017–2021) and has worked as a full‑stack developer at Jenkongklai (2022)
and SCGP (2023–present). Her experience includes backend development (Python—Django, Flask, FastAPI), frontend (React, Vue.js),
ETL pipelines and Airflow (Cloud Composer), DevOps/GCP (Cloud Run, Cloud Build, Cloud Storage, BigQuery), Docker deployments, CI/CD, IoT integration (MQTT,
WebSockets), and databases (MySQL, PostgreSQL, BigQuery, MongoDB, Redis).
```


## 📚 Learning Goals

This repository is intended for practice and learning purposes only (not production).
It’s focused on understanding how the components of a simple RAG system connect:

- Load data (PDF/text)
- Create embeddings with Hugging Face
- Store and retrieve with pgvector
- Generate answers with Ollama or OpenAI through LangChain

### RAG pipeline diagram
  <img width="2583" height="1299" alt="image" src="https://github.com/user-attachments/assets/81b3659a-bbd4-429c-9e50-7eb8d13245a3" />
  <img width="2532" height="1299" alt="image" src="https://github.com/user-attachments/assets/5bb226bd-8aee-4993-a103-5a6b649c2847" />

