#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from retrieval.retriever import DocsRetriever
from generation.generator import AnswerGenerator

app = FastAPI(title="Anthropic Docs RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Einmal beim Server-Start initialisieren
retriever = DocsRetriever()
generator = AnswerGenerator()


class QueryRequest(BaseModel):
    question: str
    k: int = 1


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    docs = retriever.retrieve(request.question, k=request.k)
    chunks = [doc.page_content for doc in docs]
    
    answer = generator.generate_answer(request.question, chunks)

    return QueryResponse(
        answer=answer,
        sources=[]  # Metadata kommt in nächstem Schritt
    )