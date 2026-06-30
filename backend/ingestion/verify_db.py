from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma(
    persist_directory="../chroma_db",
    embedding_function=embeddings,
    collection_name="anthropic_docs"
)

print(f"Anzahl gespeicherter Chunks: {vectorstore._collection.count()}")

results = vectorstore.similarity_search("What is prompt caching?", k=3)
for i, doc in enumerate(results):
    print(f"\n--- Ergebnis {i+1} ---")
    print(doc.page_content[:200])