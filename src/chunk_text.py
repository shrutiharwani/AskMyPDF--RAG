from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = "/Users/shruti/pdf_project/data/sample.pdf" 
reader = PdfReader(pdf_path)


full_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + "\n"

print("Total characters in PDF:", len(full_text))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800,
    chunk_overlap = 100
)

chunks = text_splitter.split_text(full_text)

print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks[:3]):
    print(f"---Chunk {i+1}---")
    print(chunk[:300])
    print()