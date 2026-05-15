from sentence_transformers import SentenceTransformer
import numpy as np

# Load MiniLM model (downloads once, ~80MB)
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    """
    Takes list of chunk dicts, returns numpy array of embeddings.
    Each embedding is 384-dimensional (MiniLM output).
    """
    texts = [chunk["text"] for chunk in chunks]
    print(f"[Embedder] Embedding {len(texts)} chunks...")
    
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    
    print(f"[Embedder] Embedding shape: {embeddings.shape}")
    return embeddings

def embed_query(query_text):
    """
    Embeds a single user query string into a vector.
    """
    return model.encode([query_text], convert_to_numpy=True)[0]
