from pypdf import PdfReader

pdf_path = "/Users/shruti/pdf_project/data/sample.pdf"

reader = PdfReader(pdf_path)

print(f"Number of pages: {len(reader.pages)}\n")

for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        print(f"--- Page {i+1} ---")
        print(text[:500])
        print("\n")

print("PDF reading completed.")