import fitz  # PyMuPDF

def load_pdf_chunks(pdf_path, chunk_size=300, overlap=50):
    """
    Opens a PDF and returns a list of text chunks with metadata.
    chunk_size: number of characters per chunk
    overlap: characters shared between consecutive chunks (context preservation)
    """
    doc = fitz.open(pdf_path)
    chunks = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        text = text.strip()

        if not text:
            continue

        # Slide a window over the page text
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "chunk_id": f"{pdf_path}_p{page_num}_s{start}",
                    "text": chunk_text,
                    "page": page_num + 1,
                    "file": pdf_path
                })

            start += chunk_size - overlap  # move forward with overlap

    print(f"[Chunker] Total chunks created: {len(chunks)}")
    return chunks

##checking of chunker
# Temporary test — delete this after testing
if __name__ == "__main__":
    # Put any PDF you have in the data/ folder
    chunks = load_pdf_chunks("data/sample.pdf")
    print(f"\nFirst chunk preview:")
    print(chunks[0])
