# Projektübersicht – Schritt für Schritt

## Schritt 0: Projekt Setup

- Ordnerstruktur anlegen
- venv erstellen und aktivieren
- Dependencies installieren
- .env und .gitignore anlegen
- Git initialisieren


## Schritt 1: Data Ingestion Pipeline

- Anthropic Docs scrapen (gefilterte Seiten via llms.txt)
- Text chunken (RecursiveCharacterTextSplitter)
- Chunks embedden (Sentence Transformers, lokal)
- In ChromaDB speichern (persistent, lokal)


## Schritt 2: Retrieval Pipeline

- Query embedden mit demselben Modell
- Relevante Chunks aus ChromaDB holen (Top-k)
- Metadata (Source-URL) mit zurückgeben


## Schritt 3: Generation Pipeline

- Chunks + Query als Prompt an Gemini API schicken
- Antwort mit Quellenangaben zurückgeben
- Basis-Evaluation (sind die richtigen Chunks retrieved worden?)


## Schritt 4: FastAPI Backend

- REST Endpoint /query der Retrieval + Generation zusammenhält
- Endpoint /health zum Testen
- CORS konfigurieren für React Frontend


## Schritt 5: React Frontend

- Einfaches Chat-UI
- Query abschicken, Antwort anzeigen
- Quellen (Source-URLs) unter der Antwort anzeigen


## Schritt 6: Deployment

- Backend auf Hugging Face Spaces (Docker)
- Frontend auf Hugging Face Spaces oder Vercel
- ChromaDB persistent im Space


