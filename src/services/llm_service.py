import chromadb
import ollama

VECTOR_DIR = "vector_store"
COLLECTION_NAME = "pdf_chunks"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3"


def ask_llm(question):
    # 1️⃣ Load collection
    client = chromadb.PersistentClient(path=VECTOR_DIR)
    collection = client.get_collection(name=COLLECTION_NAME)

    # 2️⃣ Embed question
    query_embedding = ollama.embeddings(
        model=EMBED_MODEL,
        prompt=question
    )["embedding"]

    # 3️⃣ Retrieve top chunks
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3   # 🔥 reduce from 4 → 3
    )

    documents = results.get("documents", [[]])[0]

    print("RETRIEVED CHUNKS:", len(documents))

    if not documents:
        return "No relevant information found in the PDF."

    # 🔥 LIMIT CONTEXT SIZE (VERY IMPORTANT)
    context = "\n\n".join(documents[:3])

    # 4️⃣ STRONG, SAFE PROMPT
    prompt = f"""
You are a PDF Question Answering assistant.

Rules:
- Use ONLY the provided context
- If answer is not in context, say: "Not found in the document"
- Answer clearly in bullet points

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()
