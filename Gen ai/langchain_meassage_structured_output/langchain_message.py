from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm =ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0.7
)


dialogue=[
    SystemMessage(content="you are a helpful python tutor"),
    HumanMessage(content="tell me about langchain framework"),
    AIMessage(content="create a gen-ai application"),
    HumanMessage(content="how to instaal it")
]

response=llm.invoke(dialogue)

dialogue.append(AIMessage(content=response.content))

print(dialogue)

