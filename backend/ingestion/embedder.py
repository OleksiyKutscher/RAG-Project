from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from chunker import load_and_chunk
import time


def build_vectorstore(filepath: str, persist_directory: str = "../chroma_db"):
    print("Lade und chunke Dokument...")
    chunks = load_and_chunk(filepath)
    chunks = [c for c in chunks if len(c.page_content) >= 50]
    print(f"{len(chunks)} Chunks nach Filterung")

    print("Lade Embedding-Modell...")
    embedding_func = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Erstelle ChromaDB (das dauert je nach Chunk-Anzahl)...")
    start = time.time()

    # In Batches einfügen, damit es nicht bei einem Fehler komplett abbricht
    batch_size = 500
    vectorstore = None

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        if vectorstore is None:
            vectorstore = Chroma.from_documents(
                documents=batch,
                embedding=embedding_func,
                persist_directory=persist_directory,
                collection_name="anthropic_docs"
            )
        else:
            vectorstore.add_documents(batch)

        elapsed = time.time() - start
        done = i + len(batch)
        print(f"{done}/{len(chunks)} Chunks ({elapsed:.0f}s)")

    print(f"Fertig in {time.time() - start:.0f}s")
    return vectorstore


if __name__ == "__main__":
    build_vectorstore("llms-full.txt")