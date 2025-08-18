from langchain_groq import ChatGroq
import os

os.environ["GROQ_API_KEY"] = "API_KEY_HERE"

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)



