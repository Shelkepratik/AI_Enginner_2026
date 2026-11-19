from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm =ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0.7
)

print("Welcome to AI Chatbot!")
print("Type 'exit' to stop the chatbot.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    response = llm.invoke(question)

    print("AI:", response.content)