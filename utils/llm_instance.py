from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "API_KEY_HERE"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4

)
