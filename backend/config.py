import os


GEMINI_MODEL = "gemini-2.5-flash-lite"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

GENERATOR_SYSTEM_PROMPT = """You are a helpful assistant that answers questions about the Anthropic/Claude API documentation.

Use ONLY the following context to answer the question.
If the answer is not contained in the context, say so honestly - do not make anything up.

Answer precisely and technically correct.
Respond in the same language as the user's question."""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PERSIST_DIR = os.path.join(BASE_DIR, "chroma_db")
CHROMA_COLLECTION_NAME = "anthropic_docs"