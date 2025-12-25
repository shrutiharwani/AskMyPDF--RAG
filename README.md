# PDF Reader RAG

A Flask-based application for chatting with PDF documents using a local Retrieval-Augmented Generation (RAG) pipeline.

---

## Architecture Style

Vertical flow (top to bottom):

Request  
→ Web Layer  
→ Application Logic  
→ RAG Processing  
→ Storage  
→ Response

---

## Project Structure

PDF_Reader_RAG/

app.py  
(config entry point)

↓  
config.py  
(application configuration)

↓  
routes/  
(HTTP request handling)

↓  
services/  
(core application logic)

↓  
rag/  
(PDF loading, embeddings, retrieval, LLM)

↓  
models/  
(data models)

↓  
database/  
(SQLite persistence)

↓  
templates/  
(UI rendering)

↓  
static/  
(CSS, JS, uploads)

↓  
requirements.txt  
.env  
README.md

---

## Technologies

Flask  
Ollama  
ChromaDB  
SQLite  

---

## Setup

Python 3.9+ required  
Ollama must be installed locally  

Pull model:

ollama pull mistral

---

## Run

python -m venv venv  
activate virtual environment  
pip install -r requirements.txt  

flask run  

Open: http://127.0.0.1:5000

---

## RAG Flow

PDF  
→ Chunking  
→ Embeddings  
→ Vector Store  
→ Retrieval  
→ Ollama  
→ Answer

---
