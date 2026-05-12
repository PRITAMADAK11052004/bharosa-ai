import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "vector_store/faiss.index"
META_PATH  = "vector_store/metadata.pkl"

def save_to_faiss(embeddings, chunks):
    """
    Builds a FAISS flat index from embeddings and saves to disk.
    Also saves chunk metadata (text, page, file) as a pickle.
    """
    os.makedirs("vector_store", exist_ok=True)

    dim = embeddings.shape[1]  # 384 for MiniLM
    index = faiss.IndexFlatL2(dim)  # L2 distance (you can also use IndexFlatIP for cosine)
    
    # Normalize for cosine similarity (optional but recommended)
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    normalized = embeddings / norms

    index.add(normalized.astype('float32'))

    # Save index
    faiss.write_index(index, INDEX_PATH)

    # Save metadata
    with open(META_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print(f"[VectorDB] Saved {index.ntotal} vectors to FAISS.")

def load_faiss():
    """
    Loads FAISS index and metadata from disk.
    """
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        chunks = pickle.load(f)
    print(f"[VectorDB] Loaded index with {index.ntotal} vectors.")
    return index, chunks

def search(query_embedding, index, chunks, top_k=5):
    """
    Searches FAISS index for top-k nearest chunks to query embedding.
    Returns list of (score, chunk_dict).
    """
    # Normalize query
    query = query_embedding / np.linalg.norm(query_embedding)
    query = query.reshape(1, -1).astype('float32')

    distances, indices = index.search(query, top_k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if idx == -1:
            continue
        results.append({
            "score": float(dist),
            "chunk": chunks[idx]
        })

    return results