# AskMyPDF-RAG

AskMyPDF-RAG is a full-stack web application that allows users to upload PDF documents and interact with them using natural language.  
The application is built using Flask and implements a Retrieval-Augmented Generation (RAG) pipeline powered by local Large Language Models (LLMs) via Ollama.

Users can register, log in, upload PDFs, and ask questions based on document content. The system retrieves relevant text chunks using vector similarity search and generates accurate answers using an LLM.

---

## Key Features

- User registration and authentication
- Secure password storage using hashing
- Profile picture upload
- PDF upload and processing
- Text chunking and embedding generation
- Vector similarity search using ChromaDB
- Question answering using local LLMs
- Persistent chat history using SQLite
- Fully local execution with no external AI API dependency
- Clean service-based backend architecture

---

## Tech Stack

- **Backend**: Python, Flask
- **LLM Runtime**: Ollama
- **Language Model**: llama3
- **Embedding Model**: nomic-embed-text
- **Vector Database**: ChromaDB (persistent)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask sessions, Werkzeug password hashing

---

## Project Structure

```text
AskMyPDF-RAG/
├── src/
│   ├── app.py                # Flask application entry point
│   ├── routes.py             # Core application routes
│   ├── auth_routes.py        # Authentication routes
│   ├── __init__.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── pdf_processor.py  # PDF parsing and embedding logic
│   │   ├── llm_service.py    # Retrieval and LLM response logic
│   │   ├── history_db.py     # Chat history persistence
│   │   └── user_db.py        # User database management
│   │
│   ├── templates/
│   │   ├── chat.html
│   │   ├── login.html
│   │   └── register.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
├── requirements.txt
├── .gitignore
└── README.md
Setup and Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/shrutiharwani/AskMyPDF--RAG.git
cd AskMyPDF--RAG
2. Create and Activate a Virtual Environment
Windows (PowerShell):

powershell
Copy code
python -m venv venv
.\venv\Scripts\activate
macOS / Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
LLM Setup
This project uses Ollama to run Large Language Models locally.
LLM model files are not included in the repository and must be downloaded separately.

1. Install Ollama
Download and install Ollama from:

bash
Copy code
https://ollama.com/download
Verify installation:

bash
Copy code
ollama --version
2. Pull Required Models
bash
Copy code
ollama pull llama3
ollama pull nomic-embed-text
3. Start the LLM Server
bash
Copy code
ollama run llama3
Keep this terminal running while using the application.
The Flask backend automatically connects to the local Ollama server.

How to Run the Application
From the project root directory:

bash
Copy code
python -m src.app
The application will be available at:

bash
Copy code
http://127.0.0.1:5000
Application Workflow
Register a new user account

Log in with registered credentials

Upload a PDF document

The PDF is processed into text chunks and embedded

Ask questions related to the uploaded document

Relevant chunks are retrieved using vector similarity

The LLM generates answers using retrieved context

Chat history is stored persistently

Notes
LLM models and vector databases are generated locally

Model files are not committed to the repository

This design follows best practices for open-source RAG systems

No external cloud-based AI services are required

Updating Requirements
bash
Copy code
pip freeze > requirements.txt
Future Enhancements
User-specific vector stores

Multiple PDF support per user

Source citations for answers

Streaming responses

Role-based access control

Deployment-ready configuration

License
This project is intended for educational and learning purposes.

yaml
Copy code

---

If you want next:
- Resume bullet points for this project  
- System design explanation  
- Interview Q&A  
- Deployment guide  

Just say the word.
