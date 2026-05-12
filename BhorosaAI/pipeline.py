"""
pipeline.py - Full System Integration for Bharosa AI
Clean, stable, and maintainable version with proper parameter handling.
"""

import os
from typing import Optional, Dict, Any
from datetime import datetime

# ── Import project modules ─────────────────────────────────────
from chunker import load_pdf_chunks
from embedder import generate_embeddings
from vector_db import index_chunks, query_vector_db
from retriever import retrieve_context
from orchestrator import orchestrate
from llm_engine import run_llm_pipeline

# Global session history for multi-turn conversation
session_history: list = []


def index_document(pdf_path: str) -> bool:
    """Index a PDF document into the vector store."""
    try:
        if not os.path.exists(pdf_path):
            print(f"[Pipeline] ❌ File not found: {pdf_path}")
            return False

        print(f"[Pipeline] 📄 Indexing: {os.path.basename(pdf_path)}")

        # 1. Chunk
        chunks = load_pdf_chunks(pdf_path)
        if not chunks:
            print("[Pipeline] ⚠️ No chunks extracted")
            return False

        # 2. Embed
        print(f"[Pipeline] 🔢 Generating embeddings for {len(chunks)} chunks...")
        chunks_with_embeddings = generate_embeddings(chunks)

        # 3. Store
        success = index_chunks(chunks_with_embeddings)
        
        if success:
            print(f"[Pipeline] ✅ Successfully indexed {len(chunks)} chunks")
            return True
        return False

    except Exception as e:
        print(f"[Pipeline] ❌ Error indexing document: {e}")
        return False


def run_full_pipeline(
    user_query: str, 
    pdf_path: Optional[str] = None,
    top_k: int = 6
) -> str:
    """
    Main Bharosa AI Pipeline
    """
    print(f"\n{'='*75}")
    print(f"🧠 BHAROSA AI - {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*75}\n")

    try:
        # ── STEP 1: Index if PDF provided ─────────────────────
        if pdf_path:
            index_document(pdf_path)

        # ── STEP 2: Retrieval ─────────────────────────────────
        print(f"[Pipeline] 🔍 Searching: '{user_query}'")
        retrieval_results = retrieve_context(user_query, top_k=top_k)

        if not retrieval_results:
            context = ""
            print("[Pipeline] ⚠️ No relevant chunks found")
        else:
            context = "\n\n".join([r["chunk"]["text"] for r in retrieval_results])
            print(f"[Pipeline] 📦 Retrieved {len(retrieval_results)} chunks")

        # ── STEP 3: Orchestration ─────────────────────────────
        print("[Pipeline] 🧩 Orchestrating...")
        orchestration = orchestrate(
            query=user_query, 
            context=context, 
            session_history=session_history   # ← Fixed: correct parameter name
        )

        if orchestration.get("action") == "silence":
            response = "Could you please be more specific about what you want to know?"
            print("[Pipeline] ❓ Clarification requested")
            return response

        print(f"[Pipeline] 🎯 Action: {orchestration.get('action')} | "
              f"Style: {orchestration.get('style')}")

        final_prompt = orchestration["prompt"]

        # ── STEP 4: LLM Generation ────────────────────────────
        print("[Pipeline] ✨ Generating response...")
        llm_result = run_llm_pipeline(
            query=final_prompt,
            context=context
            # ← Fixed: Removed extra 'history' argument
        )

        final_response = llm_result["response"]

        # Update history
        session_history.append({
            "query": user_query,
            "response": final_response,
            "timestamp": datetime.now().isoformat()
        })

        # ── Final Output ──────────────────────────────────────
        print(f"\n{'='*75}")
        print("✅ FINAL ANSWER")
        print(f"{'='*75}")
        print(final_response)
        print(f"{'='*75}\n")

        return final_response

    except Exception as e:
        print(f"[Pipeline] ❌ Critical Error: {e}")
        return "Sorry, I encountered an error. Please try again."


# ── Test Run ─────────────────────────────────────────────────
if __name__ == "__main__":
    test_query = "Explain the Hierarchical Adaptive Embedding Memory System"
    
    run_full_pipeline(
        user_query=test_query,
        pdf_path="data/Agile&Empathy_Tekathon2o.pdf",
        top_k=7
    )
