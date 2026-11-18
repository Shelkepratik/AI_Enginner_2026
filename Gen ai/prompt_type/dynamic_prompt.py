from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
llm=ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)
length=input("Enter the length of the report (short/medium/long):")
subject=input("Enter a subject on which you want to crate a report:")

prompt="prvide {} report on {}".format(length,subject)

print(prompt)

response=llm.invoke(prompt)

print(response.content)