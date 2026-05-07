from fastapi import FastAPI
from ingestion import ingest
from retriever import retrieve
from generator import generate
from rewriter import rewrite_query
app = FastAPI()

@app.get("/ingest")
def ingest_data():
    return {"msg": ingest(r"C:\Users\akshrasingh\OneDrive - Microsoft\Desktop\trial for personal proj")}

@app.get("/query")
def query(q: str):
    rewritten_query = rewrite_query(q)
    docs = retrieve(rewritten_query)
    answer = generate(q, docs)
    return {
        "original_query": q,
        "rewritten_query": rewritten_query,
        "answer": answer
    }
    docs = retrieve(rewritten_query)

    answer = generate(q, docs)

    return {
        "original_query": q,
        "rewritten_query": rewritten_query,
        "answer": answer
    }