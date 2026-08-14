# Anthropic Docs RAG

A retrieval-augmented generation (RAG) system for semantic search and question answering over the Anthropic/Claude API documentation. Built to demonstrate end-to-end LLM application development – from data ingestion to a conversational frontend.

> **Note:** Anthropic provides an official documentation chatbot. This project independently implements the underlying RAG pipeline from scratch to demonstrate the engineering behind such systems.

---

## Architecture

```
User Query
    │
    ▼
[React Frontend]
    │  HTTP POST /query
    ▼
[FastAPI Backend]
    ├── [DocsRetriever]  →  ChromaDB (vector search)
    │       └── Sentence Transformers (embedding)
    └── [AnswerGenerator]  →  Gemini API (generation)
    │
    ▼
Answer + Sources
```

---

## Tech Stack

| Layer | Technology | Role |
|---|---|---|
| Data Ingestion | LangChain `RecursiveCharacterTextSplitter` | Splits documentation into ~1500-character chunks |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` | Local embedding model, no API cost |
| Vector Store | ChromaDB | Persistent vector database, ~75k chunks |
| Retrieval | LangChain + ChromaDB | Cosine similarity search, top-k chunks |
| Generation | Gemini API (`gemini-2.5-flash-lite`) via `langchain-google-genai` | Answer generation grounded in retrieved chunks |
| Backend | FastAPI + Uvicorn | REST API, CORS, request validation via Pydantic |
| Frontend | React + Vite | Chat UI, Axios for API communication |

---

## Project Structure

```
rag-project/
├── backend/
│   ├── ingestion/
│   │   ├── chunker.py        # Text splitting
│   │   └── embedder.py       # Embedding + ChromaDB setup
│   ├── retrieval/
│   │   └── retriever.py      # DocsRetriever class
│   ├── generation/
│   │   └── generator.py      # AnswerGenerator class
│   ├── api/
│   │   └── main.py           # FastAPI endpoints
│   ├── chroma_db/            # Persistent vector store (not in git)
│   ├── config.py             # Central configuration
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatMessage.jsx
│   │   │   └── ChatInput.jsx
│   │   ├── api/
│   │   │   └── client.js
│   │   └── App.jsx
│   └── package.json
└── README.md
```

---

## Setup

### Prerequisites

- Python 3.10+
- Node.js 18+
- Gemini API Key ([aistudio.google.com](https://aistudio.google.com))

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:
```
GEMINI_API_KEY=your_key_here
```

Build the vector store (one-time):
```bash
# Download anthropic_docs.txt from https://docs.claude.com/llms-full.txt
cd ingestion
python embedder.py
```

Start the server:
```bash
cd backend
fastapi dev api/main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`

---

## Usage

The system answers questions about the Anthropic/Claude API documentation based strictly on retrieved content – no hallucination, as the model is instructed to only use the provided context chunks.

**Example questions:**

- *"How does prompt caching reduce latency?"*
- *"What is the difference between streaming and non-streaming responses?"*
- *"How do I implement tool use with Claude?"*
- *"What are the token limits for different Claude models?"*

---

## Knowledge Base

The knowledge base is built from `llms-full.txt` at [docs.claude.com](https://docs.claude.com/llms-full.txt) – a machine-readable full export of the Anthropic documentation. After chunking (chunk_size=1500, overlap=200) and filtering, approximately 75,000 chunks are embedded and stored in ChromaDB.
