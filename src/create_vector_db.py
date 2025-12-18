from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import ollama
import os

# --------------------
# CONFIG
# --------------------
PDF_PATH = "/Users/shruti/pdf_project/data/sample.pdf"
CHROMA_DIR = "/Users/shruti/pdf_project/vector_store"
COLLECTION_NAME = "pdf_chunks"
EMBED_MODEL = "nomic-embed-text"

# --------------------
# ENSURE DIRECTORY EXISTS
# --------------------
os.makedirs(CHROMA_DIR, exist_ok=True)

# --------------------
# LOAD PDF
# --------------------
reader = PdfReader(PDF_PATH)

full_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"

print("PDF loaded.")

# --------------------
# CHUNKING
# --------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_text(full_text)
print(f"Total chunks: {len(chunks)}")

# --------------------
# PERSISTENT CHROMA CLIENT (🔥 FIX)
# --------------------
client = chromadb.PersistentClient(path=CHROMA_DIR)

# FORCE CLEAN REBUILD
existing = [c.name for c in client.list_collections()]
if COLLECTION_NAME in existing:
    client.delete_collection(name=COLLECTION_NAME)

collection = client.get_or_create_collection(name=COLLECTION_NAME)

# --------------------
# CREATE & STORE EMBEDDINGS
# --------------------
print("Creating embeddings and storing them...")

embeddings = []
ids = []

for i, chunk in enumerate(chunks):
    emb = ollama.embeddings(
        model=EMBED_MODEL,
        prompt=chunk
    )["embedding"]

    embeddings.append(emb)
    ids.append(str(i))

collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=ids
)

print("Vector database created successfully!")
