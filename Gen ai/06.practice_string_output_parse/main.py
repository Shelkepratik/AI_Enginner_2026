"""(Word Meaning Finder)."""
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)

word=input("enter an English word: ")

prompt=f"Give the meaning of the word '{word}' in one simple line and one example sentence."

respose=llm.invoke(prompt)

print("\nFull Response:")
print(respose)

#create stroutputparser object
parser_obj=StrOutputParser()
final_result=parser_obj.invoke(respose)

print("\nfinal result:")
print(final_result)

print("\n result Type: ")
print(type(final_result))



