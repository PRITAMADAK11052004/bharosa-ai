"""
Bharosa AI — Reasoning Orchestrator
Team: Agile & Empathy
 
Architecture:
    USER QUERY
        ↓
    [Heap 1] Cognitive Urgency Layer   → Should system respond?
        ↓
    [Heap 2] Action Deliberation Layer → What should it do?
        ↓
    [Heap 3] Expression Strategy Layer → How should it sound?
        ↓
    Prompt Builder
        ↓
    Qwen LLM
        ↓
    Final Response
"""
 
import heapq
 
 
# ══════════════════════════════════════════════════════════════
# LAYER 1 — COGNITIVE URGENCY HEAP
# Decides: Should the system respond at all?
# ══════════════════════════════════════════════════════════════
 
def urgency_layer(query, context, session_history=None):
    """
    Scores the query on multiple urgency signals.
    If total urgency is too low → system stays silent or asks clarification.
    Priority = base_score + context_bonus - repetition_penalty
    """
    query_lower = query.lower()
    heap        = []
 
    if session_history is None:
        session_history = []
 
    # ── Repetition penalty ──────────────────────────────────
    # If user asked same/similar thing recently, reduce urgency
    repetition_penalty = 0
    for past_query in session_history[-5:]:   # check last 5 queries
        if past_query.lower().strip() == query_lower.strip():
            repetition_penalty = 4            # strong penalty for exact repeat
            break
        shared_words = set(query_lower.split()) & set(past_query.lower().split())
        if len(shared_words) > 3:
            repetition_penalty = max(repetition_penalty, 2)  # mild penalty
 
    # ── Signal scoring ──────────────────────────────────────
    signals = {
        "urgency": {
            "keywords": ["urgent", "asap", "immediately", "important", "critical"],
            "base":     8,
            "bonus":    3 if any(k in query_lower for k in ["urgent", "critical"]) else 0
        },
        "novelty": {
            "keywords": [],
            "base":     5,
            # bonus if query words are NOT in recent history
            "bonus":    2 if not any(query_lower in h.lower() for h in session_history) else 0
        },
        "emotional_weight": {
            "keywords": ["help", "please", "need", "confused", "stuck", "struggling"],
            "base":     4,
            "bonus":    2 if any(k in query_lower for k in ["please", "help", "struggling"]) else 0
        },
        "ambiguity": {
            "keywords": ["maybe", "not sure", "i think", "something about", "kind of"],
            "base":     3,
            "bonus":    0
        },
        "context_richness": {
            "keywords": [],
            "base":     6 if len(context.split()) > 50 else 2,  # rich context = higher urgency
            "bonus":    0
        }
    }
 
    for signal_name, props in signals.items():
        keyword_matched = any(k in query_lower for k in props["keywords"])
        score = props["base"] + props["bonus"] - repetition_penalty
 
        # Only push if this signal is relevant
        if props["keywords"] == [] or keyword_matched or signal_name in ["novelty", "context_richness"]:
            score = max(0, score)  # no negative scores
            heapq.heappush(heap, (-score, signal_name))
 
    if not heap:
        return False, "silence", 0
 
    # Top signal from heap
    top_neg_score, top_signal = heapq.heappop(heap)
    final_urgency = -top_neg_score
 
    # Threshold: if urgency < 3, do not respond
    if final_urgency < 3:
        return False, "silence", final_urgency
 
    return True, top_signal, final_urgency
 
 
# ══════════════════════════════════════════════════════════════
# LAYER 2 — ACTION DELIBERATION HEAP
# Decides: WHAT kind of response to give
# ══════════════════════════════════════════════════════════════
 
def action_layer(query, urgency_signal):
    """
    Detects the best action using keyword matching + dynamic priority scoring.
    Priority = base_score + context_bonus - repetition_penalty (adaptive)
    """
    query_lower = query.lower()
    heap        = []
 
    # ── Action rules ────────────────────────────────────────
    # Format: action_name → (keywords, base_priority)
    action_rules = {
        "comparison": {
            "keywords": ["compare", "difference", "vs", "versus", "better", "contrast", "which is"],
            "base":     8
        },
        "explanation": {
            "keywords": ["explain", "what is", "how does", "describe", "define", "tell me about"],
            "base":     7
        },
        "summarization": {
            "keywords": ["summarize", "summary", "brief", "overview", "shorten", "tldr"],
            "base":     6
        },
        "listing": {
            "keywords": ["list", "give me", "show all", "what are", "enumerate", "mention"],
            "base":     5
        },
        "retrieval": {
            "keywords": ["find", "search", "where", "locate", "retrieve", "get"],
            "base":     4
        },
        "clarification": {
            "keywords": ["maybe", "not sure", "i think", "something about", "kind of", "unclear"],
            "base":     3
        },
        "explanation": {
            "keywords": ["confused", "stuck", "struggling", "lost", "dont understand", "don't understand", "help me understand"],
            "base":     7
        },
    }
 
    matched_any = False
 
    for action_name, props in action_rules.items():
        match_count = sum(1 for kw in props["keywords"] if kw in query_lower)
 
        if match_count > 0:
            matched_any = True
 
            # Adaptive priority:
            # base + (bonus per extra keyword match) + urgency bonus
            urgency_bonus = 2 if urgency_signal in ["urgency", "emotional_weight"] else 0
            adaptive_score = props["base"] + (match_count * 1) + urgency_bonus
 
            heapq.heappush(heap, (-adaptive_score, match_count, action_name))
 
    if not matched_any:
        return "general", 0
 
    neg_score, match_count, best_action = heapq.heappop(heap)
    return best_action, -neg_score
 
 
# ══════════════════════════════════════════════════════════════
# LAYER 3 — EXPRESSION STRATEGY HEAP
# Decides: HOW the response should sound / feel
# ══════════════════════════════════════════════════════════════
 
def expression_layer(action, urgency_signal, query):
    """
    Selects response style based on action type and urgency signal.
    Different actions and emotional states need different expression styles.
    """
    query_lower = query.lower()
    heap        = []
 
    # ── Style rules ─────────────────────────────────────────
    # Format: style → (base_score, boost_condition)
    style_rules = {
        "educational": {
            "base":  9,
            "boost": action in ["explanation", "listing"]
        },
        "analytical": {
            "base":  8,
            "boost": action in ["comparison", "retrieval"]
        },
        "concise": {
            "base":  6,
            "boost": action in ["summarization", "general"]
        },
        "empathetic": {
            "base":  5,
            "boost": urgency_signal == "emotional_weight"
        },
        "calm": {
            "base":  4,
            "boost": any(w in query_lower for w in ["confused", "stuck", "lost", "help"])
        },
        "structured": {
            "base":  7,
            "boost": action == "comparison"
        }
    }
 
    for style_name, props in style_rules.items():
        boost_score = 3 if props["boost"] else 0
        final_score = props["base"] + boost_score
        heapq.heappush(heap, (-final_score, style_name))
 
    neg_score, best_style = heapq.heappop(heap)
    return best_style, -neg_score
 
 
# ══════════════════════════════════════════════════════════════
# PROMPT BUILDER
# Combines query + context + action + style → final LLM prompt
# ══════════════════════════════════════════════════════════════
 
def build_prompt(query, context, action, style):
    """Builds the final prompt for Qwen based on action + style."""
 
    # Style tone instructions
    style_instructions = {
        "educational":  "Explain clearly and educationally. Use examples if helpful.",
        "analytical":   "Be precise and analytical. Use structured points.",
        "concise":      "Be brief and to the point. No unnecessary words.",
        "empathetic":   "Be warm, supportive, and easy to understand.",
        "calm":         "Respond in a calm, reassuring, and clear manner.",
        "structured":   "Use headers or bullet points. Be very organized."
    }
 
    base = (
        "You are Bharosa AI, a helpful offline personal AI assistant. "
        "Answer ONLY based on the provided context. "
        "Do NOT make up information not present in the context. "
        f"{style_instructions.get(style, '')}"
    )
 
    if action == "comparison":
        return f"""{base}
 
Context:
{context}
 
Task: Compare the topics in the question. Use bullet points or a structured format.
Question: {query}
 
Comparison:"""
 
    elif action == "explanation":
        return f"""{base}
 
Context:
{context}
 
Task: Explain the concept clearly. Use step-by-step if needed.
Question: {query}
 
Explanation:"""
 
    elif action == "summarization":
        return f"""{base}
 
Context:
{context}
 
Task: Write a clear, concise summary of the above context.
 
Summary:"""
 
    elif action == "listing":
        return f"""{base}
 
Context:
{context}
 
Task: List all relevant items clearly and completely.
Question: {query}
 
List:"""
 
    elif action == "retrieval":
        return f"""{base}
 
Context:
{context}
 
Task: Find and return the most relevant information for the question.
Question: {query}
 
Answer:"""
 
    elif action == "clarification":
        return f"""{base}
 
Context:
{context}
 
The question seems unclear. Ask the user one focused clarifying question 
to understand what they actually want.
Question: {query}
 
Clarification Request:"""
 
    else:  # general
        return f"""{base}
 
Context:
{context}
 
Question: {query}
 
Answer:"""
 
 
# ══════════════════════════════════════════════════════════════
# MAIN ORCHESTRATOR
# Combines all 3 layers into one clean function
# ══════════════════════════════════════════════════════════════
 
def orchestrate(query, context, session_history=None):
    """
    Main entry point for the Reasoning Orchestrator.
 
    Args:
        query           : User's natural language query (str)
        context         : Retrieved chunks from Member 3 (str)
        session_history : List of past queries in this session (list)
 
    Returns:
        dict with model, action, style, urgency, prompt
        OR dict with action="silence" if query is not worth responding to
    """
 
    if session_history is None:
        session_history = []
 
    # ── Layer 1: Should we respond? ──────────────────────────
    should_respond, urgency_signal, urgency_score = urgency_layer(
        query, context, session_history
    )
 
    if not should_respond:
        return {
            "model":          "qwen",
            "action":         "silence",
            "urgency_signal": urgency_signal,
            "urgency_score":  urgency_score,
            "style":          None,
            "prompt":         None,
            "note":           "Query urgency too low. Consider asking for clarification."
        }
 
    # ── Layer 2: What to do? ─────────────────────────────────
    action, action_score = action_layer(query, urgency_signal)
 
    # ── Layer 3: How to express it? ──────────────────────────
    style, style_score = expression_layer(action, urgency_signal, query)
 
    # ── Build final prompt ───────────────────────────────────
    prompt = build_prompt(query, context, action, style)
 
    return {
        "model":          "qwen",           # always Qwen
        "action":         action,
        "action_score":   action_score,
        "style":          style,
        "style_score":    style_score,
        "urgency_signal": urgency_signal,
        "urgency_score":  urgency_score,
        "prompt":         prompt
    }
 