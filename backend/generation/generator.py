import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
#import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import GEMINI_MODEL, GENERATOR_SYSTEM_PROMPT

load_dotenv()




class AnswerGenerator:
    def __init__(self, model: str = GEMINI_MODEL, system_prompt: str = GENERATOR_SYSTEM_PROMPT):
        self.llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=os.getenv("GEMINI_API_KEY"),
        )
        self.system_prompt = system_prompt
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "CONTEXT:\n{context}\n\nQUESTION: {query}"),
        ])
        self.chain = self.prompt_template | self.llm

    def generate_answer(self, query: str, context_chunks: list[str]) -> str:
        context = "\n\n---\n\n".join(context_chunks)
        response = self.chain.invoke({"context": context, "query": query})
        return response.content


"""
if __name__ == "__main__":
    import sys
    sys.path.append("../retrieval")
    from retriever import DocsRetriever

    retriever = DocsRetriever()
    generator = AnswerGenerator()
    query = "How does prompt caching reduce latency?"

    results = retriever.retrieve(query, k=1)
    chunks = [doc.page_content for doc in results]

    answer = generator.generate_answer(query, chunks)
    print(f"FRAGE: {query}\n")
    print(f"ANTWORT:\n{answer}")
"""