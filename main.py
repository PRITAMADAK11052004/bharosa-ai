from orchestrator.orchestrator import orchestrate


query = "Compare CNN and Transformer"

context = """
CNN uses convolution operations.
Transformer uses attention mechanism.
"""

result = orchestrate(query, context)

print(result)