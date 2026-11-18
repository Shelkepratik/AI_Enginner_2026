from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

tmpl="write a poem about {subject} in a {tone} tone with {lines} lines"


prompt_obj=PromptTemplate(
    template=tmpl
)

subject=input("provide a subject:")
tone=input("provide the tone:")
lines=int(input("Enter the lines of poem to create:"))

complete_prompt=prompt_obj.invoke(
    {
        "subject":subject,
        "tone":tone,
        "lines":lines
    }
)
print(complete_prompt)
print(complete_prompt.text)
final_prompt=complete_prompt.text

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)
result=llm.invoke(final_prompt)
print(result)#the check whether how many token,which api is use find this imformation
print(result.content)
