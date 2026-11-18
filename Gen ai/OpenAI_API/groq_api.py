from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
     api_key=os.getenv("openai_api_key"),
    temperature=0
)

response = llm.invoke("What is the capital of China?")

print(response.content)
