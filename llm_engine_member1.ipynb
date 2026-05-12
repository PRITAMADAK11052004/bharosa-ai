{
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.10.0"}
 },
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# LLM Engine — Member 1\n",
    "**Role:** AI Runtime + Model Integration  \n",
    "**Responsibilities:** Install & run Qwen, test prompts, Python→LLM connection, response generation pipeline, LoRA (later)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## Step 1: Install Required Libraries"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Install libraries needed to load and run the Qwen model\n",
    "!pip install transformers accelerate torch"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## Step 2: Load the Qwen Model"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "import torch\n",
    "from transformers import AutoTokenizer, AutoModelForCausalLM\n",
    "\n",
    "# Load Qwen2.5-1.5B-Instruct from HuggingFace\n",
    "# float16 reduces memory usage (fits 16GB RAM), device_map='auto' uses GPU if available\n",
    "MODEL_NAME = \"Qwen/Qwen2.5-1.5B-Instruct\"\n",
    "\n",
    "tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)\n",
    "\n",
    "model = AutoModelForCausalLM.from_pretrained(\n",
    "    MODEL_NAME,\n",
    "    torch_dtype=torch.float16,\n",
    "    device_map=\"auto\"\n",
    ")\n",
    "\n",
    "print(f\"Model loaded on: {model.device}\")\n",
    "print(f\"Model parameters: {sum(p.numel() for p in model.parameters()) / 1e9:.2f}B\")"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## Step 3: Test — Basic Prompt"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Quick sanity check: send a simple greeting and verify the model responds\n",
    "messages = [\n",
    "    {\"role\": \"user\", \"content\": \"Hello, who are you?\"}\n",
    "]\n",
    "\n",
    "text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\n",
    "inputs = tokenizer(text, return_tensors=\"pt\").to(model.device)\n",
    "\n",
    "outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, do_sample=True)\n",
    "print(tokenizer.decode(outputs[0], skip_special_tokens=True))"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## Step 4: Build the Response Generation Function"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "def generate_response(query: str, context: str = \"\", max_tokens: int = 200) -> str:\n",
    "    \"\"\"\n",
    "    Core LLM function — takes a user query and optional context, returns a generated response.\n",
    "\n",
    "    Args:\n",
    "        query:      The user's question or instruction.\n",
    "        context:    Optional retrieved text (for RAG). Injected into the prompt if provided.\n",
    "        max_tokens: Maximum number of new tokens to generate.\n",
    "\n",
    "    Returns:\n",
    "        Generated response string.\n",
    "    \"\"\"\n",
    "    # Build the prompt — include context if provided (RAG-ready)\n",
    "    if context:\n",
    "        prompt = (\n",
    "            \"Answer the question using only the provided context.\\n\\n\"\n",
    "            f\"Context:\\n{context}\\n\\n\"\n",
    "            f\"Question:\\n{query}\"\n",
    "        )\n",
    "    else:\n",
    "        prompt = query\n",
    "\n",
    "    # Format as chat message\n",
    "    messages = [{\"role\": \"user\", \"content\": prompt}]\n",
    "\n",
    "    # Apply the model's chat template\n",
    "    text = tokenizer.apply_chat_template(\n",
    "        messages,\n",
    "        tokenize=False,\n",
    "        add_generation_prompt=True\n",
    "    )\n",
    "\n",
    "    # Tokenize and move to model device\n",
    "    inputs = tokenizer(text, return_tensors=\"pt\").to(model.device)\n",
    "\n",
    "    # Generate\n",
    "    outputs = model.generate(\n",
    "        **inputs,\n",
    "        max_new_tokens=max_tokens,\n",
    "        temperature=0.7,\n",
    "        do_sample=True\n",
    "    )\n",
    "\n",
    "    # Decode and return only the new tokens (strip the input prompt)\n",
    "    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)\n",
    "    \n",
    "    # Extract only the assistant's reply (after the user turn)\n",
    "    if \"assistant\" in full_output.lower():\n",
    "        response = full_output.split(\"assistant\")[-1].strip()\n",
    "    else:\n",
    "        response = full_output.strip()\n",
    "\n",
    "    return response"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## Step 5: Test — generate_response() Without Context"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Test the function with a plain query (no context / no RAG)\n",
    "response = generate_response(\"Explain recursion simply\")\n",
    "print(response)"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## Step 6: Test — generate_response() With Context (RAG-ready)"]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# Simulate what happens when another team member passes retrieved context to the LLM\n",
    "# In the full project, context will come from the retrieval pipeline (FAISS + embeddings)\n",
    "sample_context = (\n",
    "    \"Recursion is a programming technique where a function calls itself \"\n",
    "    \"to solve a smaller version of the same problem. \"\n",
    "    \"Every recursive function must have a base case to stop the recursion.\"\n",
    ")\n",
    "\n",
    "query = \"What is recursion and why does it need a base case?\"\n",
    "response = generate_response(query, context=sample_context)\n",
    "print(response)"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7: Final Pipeline — Integration-Ready Function\n",
    "This is the function that other team members call. It accepts a query + context and returns a clean string response."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "def run_llm_pipeline(query: str, context: str = \"\") -> dict:\n",
    "    \"\"\"\n",
    "    Final response generation pipeline — integration point for other team members.\n",
    "\n",
    "    Input:  query (str) + optional context (str) from retrieval pipeline\n",
    "    Output: dict with 'query', 'context_used', and 'response' keys\n",
    "    \"\"\"\n",
    "    response = generate_response(query, context=context, max_tokens=300)\n",
    "\n",
    "    return {\n",
    "        \"query\": query,\n",
    "        \"context_used\": bool(context),\n",
    "        \"response\": response\n",
    "    }\n",
    "\n",
    "\n",
    "# --- Test the final pipeline ---\n",
    "result = run_llm_pipeline(\n",
    "    query=\"What is recursion?\",\n",
    "    context=\"Recursion is when a function calls itself with a simpler input until it reaches a base case.\"\n",
    ")\n",
    "\n",
    "print(f\"Query        : {result['query']}\")\n",
    "print(f\"Context used : {result['context_used']}\")\n",
    "print(f\"Response     :\\n{result['response']}\")"
   ],
   "outputs": [],
   "execution_count": null
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8: LoRA Fine-tuning Setup (Placeholder — To Do Later)\n",
    "> This section is reserved for LoRA adapter integration once the base pipeline is validated."
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# TODO (Later): Load a LoRA adapter on top of the base Qwen model\n",
    "#\n",
    "# !pip install peft\n",
    "#\n",
    "# from peft import PeftModel\n",
    "#\n",
    "# lora_model = PeftModel.from_pretrained(\n",
    "#     model,                         # base model already loaded above\n",
    "#     \"path/to/your-lora-adapter\"    # replace with actual adapter path\n",
    "# )\n",
    "#\n",
    "# Then pass lora_model wherever 'model' is used in generate_response()\n",
    "\n",
    "print(\"LoRA placeholder ready — uncomment and fill in adapter path when needed.\")"
   ],
   "outputs": [],
   "execution_count": null
  }
 ]
}
