"""
Bharosa AI — LLM Engine
Team: Agile & Empathy

Role        : AI Runtime + Model Integration
Member      : 1
Responsibilities:
    - Load and run Qwen2.5-1.5B-Instruct
    - Response generation pipeline
    - RAG-ready context injection
    - LoRA placeholder (later)
"""

# ══════════════════════════════════════════════════════════════
# STEP 1 — INSTALL LIBRARIES
# Run this once in terminal before running this file:
#   pip install transformers accelerate torch
# ══════════════════════════════════════════════════════════════

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


# ══════════════════════════════════════════════════════════════
# STEP 2 — LOAD THE QWEN MODEL
# ══════════════════════════════════════════════════════════════

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,   # float16 reduces memory usage
    device_map="auto"            # uses GPU if available, else CPU
)

print(f"Model loaded on  : {model.device}")
print(f"Model parameters : {sum(p.numel() for p in model.parameters()) / 1e9:.2f}B")


# ══════════════════════════════════════════════════════════════
# STEP 3 — CORE RESPONSE GENERATION FUNCTION
# ══════════════════════════════════════════════════════════════

def generate_response(query: str, context: str = "", max_tokens: int = 200) -> str:
    """
    Core LLM function.
    Takes a user query and optional context, returns a generated response.

    Args:
        query      : The user's question or instruction.
        context    : Optional retrieved text (for RAG). Injected into prompt if provided.
        max_tokens : Maximum number of new tokens to generate.

    Returns:
        Generated response string.
    """

    # Build prompt — include context if provided (RAG-ready)
    if context:
        prompt = (
            "Answer the question using only the provided context.\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{query}"
        )
    else:
        prompt = query

    # Format as chat message
    messages = [{"role": "user", "content": prompt}]

    # Apply Qwen's chat template
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # Tokenize and move to model device
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    # Generate response
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.7,
        do_sample=True
    )

    # Decode full output
    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only assistant's reply
    if "assistant" in full_output.lower():
        response = full_output.split("assistant")[-1].strip()
    else:
        response = full_output.strip()

    return response


# ══════════════════════════════════════════════════════════════
# STEP 4 — FINAL PIPELINE (integration point for other members)
# ══════════════════════════════════════════════════════════════

def run_llm_pipeline(query: str, context: str = "") -> dict:
    """
    Final response generation pipeline.
    This is the function other team members call.

    Args:
        query   : User's natural language query (str)
        context : Retrieved chunks from Member 3 / prompt from Member 4 (str)

    Returns:
        dict with keys: query, context_used, response
    """
    response = generate_response(query, context=context, max_tokens=300)

    return {
        "query":        query,
        "context_used": bool(context),
        "response":     response
    }


# ══════════════════════════════════════════════════════════════
# STEP 5 — LoRA PLACEHOLDER (do later)
# ══════════════════════════════════════════════════════════════

# TODO: Load a LoRA adapter on top of the base Qwen model
#
# !pip install peft
#
# from peft import PeftModel
#
# lora_model = PeftModel.from_pretrained(
#     model,                          # base model already loaded above
#     "path/to/your-lora-adapter"     # replace with actual adapter path
# )
#
# Then pass lora_model wherever 'model' is used in generate_response()


# ══════════════════════════════════════════════════════════════
# STEP 6 — TEST (runs when you execute this file directly)
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # Test 1: Basic prompt — no context
    print("\n" + "═" * 60)
    print("TEST 1 — Basic prompt (no context)")
    print("═" * 60)
    response = generate_response("Explain recursion simply")
    print(response)

    # Test 2: RAG-ready — with context
    print("\n" + "═" * 60)
    print("TEST 2 — With context (RAG)")
    print("═" * 60)
    sample_context = (
        "Recursion is a programming technique where a function calls itself "
        "to solve a smaller version of the same problem. "
        "Every recursive function must have a base case to stop the recursion."
    )
    response = generate_response(
        "What is recursion and why does it need a base case?",
        context=sample_context
    )
    print(response)

    # Test 3: Full pipeline
    print("\n" + "═" * 60)
    print("TEST 3 — Full pipeline (run_llm_pipeline)")
    print("═" * 60)
    result = run_llm_pipeline(
        query="What is recursion?",
        context="Recursion is when a function calls itself with a simpler input until it reaches a base case."
    )
    print(f"Query        : {result['query']}")
    print(f"Context used : {result['context_used']}")
    print(f"Response     :\n{result['response']}")
