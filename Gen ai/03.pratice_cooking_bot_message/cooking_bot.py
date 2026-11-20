from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)

message=[SystemMessage(content="You are a friendly Indian cooking assistant. Give answers in simple steps,in not more than 5 lines")]


print("AI Chatbot started....")
print("Type 'exit' to stop\n")

while True:
    question=input("you: ")

    if question.lower()=="exit":
        print("Thankyou for visiting chatbot!")
        break

    message.append(HumanMessage(content=question))


    response=llm.invoke(message)

    print("AI:",response.content)

    message.append(AIMessage(content=response.content))

    print("\n chat History: ",message)