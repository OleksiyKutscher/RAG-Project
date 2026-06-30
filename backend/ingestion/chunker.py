from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import statistics


def load_and_chunk(filepath: str) -> list[Document]:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        separators=["\n# ", "\n## ", "\n### ", "\n\n", "\n", " ", ""],
    )

    chunks = splitter.create_documents([text])

    # Einfache laufende ID als Metadata, hilfreich fürs Debugging später
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i

    return chunks


if __name__ == "__main__":
    chunks = load_and_chunk("llms-full.txt")
    print(f"Anzahl Chunks: {len(chunks)}")
    print("--- Erster Chunk ---")
    print(chunks[0].page_content[:300])
    print("--- Letzter Chunk ---")
    print(chunks[-1].page_content[:300])
    lengths = [len(c.page_content) for c in chunks]
    print(f"Min: {min(lengths)}, Max: {max(lengths)}, Median: {statistics.median(lengths)}, Mean: {statistics.mean(lengths):.0f}")
    chunks = [c for c in chunks if len(c.page_content) >= 50]
    print(f"Nach Filter: {len(chunks)} Chunks")