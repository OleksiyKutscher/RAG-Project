from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import EMBEDDING_MODEL, CHROMA_PERSIST_DIR, CHROMA_COLLECTION_NAME


class DocsRetriever:
    def __init__(
        self,
        persist_directory: str = CHROMA_PERSIST_DIR,
        collection_name: str = CHROMA_COLLECTION_NAME,
        embedding_model: str = EMBEDDING_MODEL,
    ):
        print(f"Load ChromaDB from {persist_directory} (Collection: {collection_name})...")
        print(f"Using embedding model: {embedding_model}")
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings,
            collection_name=collection_name,
        )

    def retrieve(self, query: str, k: int = 4) -> list[Document]:
        """Holt die k relevantesten Chunks für eine Query."""
        print(f"Retrieving top {k} chunks for query: {query}")
        return self.vectorstore.similarity_search(query, k=k)

    def retrieve_with_scores(self, query: str, k: int = 4) -> list[tuple[Document, float]]:
        """Wie retrieve, aber inkl. Similarity-Score - nützlich für Debugging/Threshold."""
        return self.vectorstore.similarity_search_with_relevance_scores(query, k=k)

    def retrieve_filtered(self, query: str, k: int = 4, min_score: float = 0.35):
        results = self.retrieve_with_scores(query, k=k)
        return [(doc, score) for doc, score in results if score >= min_score]

"""
if __name__ == "__main__":
    retriever = DocsRetriever()

    query = "How does prompt caching reduce latency?"
    results = retriever.retrieve(query, k=4)

    for i, doc in enumerate(results):
        print(f"\n--- Ergebnis {i+1}")# (Score: {score:.3f}) ---")
        print(doc.page_content[:200])
"""