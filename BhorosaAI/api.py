from fastapi import FastAPI
from pydantic import BaseModel
from pipeline import run_full_pipeline

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_ai(req: QueryRequest):
    response = run_full_pipeline(
        user_query=req.query,
        pdf_path=None,   # already indexed
        top_k=7
    )
    return {"response": response}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins for now
    allow_methods=["*"],
    allow_headers=["*"],
)
