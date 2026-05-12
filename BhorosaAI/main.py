from retriever import index_document, query_documents

# STEP 1: Index your PDF
index_document("data/Agile&Empathy_Tekathon2o.pdf")

# STEP 2: Query it
results = query_documents("What is offline multimodal AI system?", top_k=5)