from chunker import load_pdf_chunks
from embedder import embed_chunks, embed_query
from vector_db import save_to_faiss, load_faiss, search
import os

def index_document(pdf_path):
    """
    Full indexing pipeline:
    PDF → Chunks → Embeddings → FAISS
    """
    print(f"\n=== Indexing: {pdf_path} ===")
    chunks     = load_pdf_chunks(pdf_path)
    embeddings = embed_chunks(chunks)
    save_to_faiss(embeddings, chunks)
    print("=== Indexing Complete ===\n")

def query_documents(user_query, top_k=5):
    """
    Full retrieval pipeline:
    Query → Embedding → FAISS Search → Top-K Chunks
    """
    print(f"\n=== Query: '{user_query}' ===")

    if not os.path.exists("vector_store/faiss.index"):
        print("[ERROR] No index found. Run index_document() first.")
        return []

    index, chunks = load_faiss()
    query_emb     = embed_query(user_query)
    results       = search(query_emb, index, chunks, top_k=top_k)

    print(f"\n--- Top {top_k} Results ---")
    for i, r in enumerate(results):
        print(f"\n[{i+1}] Score: {r['score']:.4f}")
        print(f"     File : {r['chunk']['file']}")
        print(f"     Page : {r['chunk']['page']}")
        print(f"     Text : {r['chunk']['text'][:200]}...")

    return results
