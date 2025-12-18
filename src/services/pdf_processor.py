from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import ollama

VECTOR_DIR = "vector_store"
COLLECTION_NAME = "pdf_chunks"
EMBED_MODEL = "nomic-embed-text"


def process_pdf(pdf_path):
    # 1️⃣ Read PDF
    reader = PdfReader(pdf_path)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    # 2️⃣ Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunks = splitter.split_text(full_text)

    # 3️⃣ Chroma client
    client = chromadb.PersistentClient(path=VECTOR_DIR)

    # Clear old PDF data
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    # 4️⃣ Create embeddings
    for i, chunk in enumerate(chunks):
        embedding = ollama.embeddings(
            model=EMBED_MODEL,
            prompt=chunk
        )["embedding"]

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk_{i}"]
        )

    print(f"✅ Stored {len(chunks)} chunks")
