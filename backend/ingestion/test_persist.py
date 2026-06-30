from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

# Mini-Test mit nur 3 Dokumenten
test_docs = [
    Document(page_content="Anthropic entwickelt Claude, ein KI-Sprachmodell."),
    Document(page_content="RAG kombiniert Retrieval mit Textgenerierung."),
    Document(page_content="ChromaDB ist eine Vektordatenbank."),
]

print("Lade Embedding-Modell...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

print("Erstelle Test-ChromaDB...")
vectorstore = Chroma.from_documents(
    documents=test_docs,
    embedding=embeddings,
    persist_directory="../chroma_db_test",
    collection_name="test_collection"
)

print("Test-Query...")
results = vectorstore.similarity_search("Was ist eine Vektordatenbank?", k=1)
print(f"Ergebnis: {results[0].page_content}")

print("Fertig - prüfe ob der Ordner '../chroma_db_test' existiert")