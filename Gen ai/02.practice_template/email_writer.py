from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

tmle="Write a {tone} email to {receiver} about {topic}. Keep it under {words} words and end it with the name {sender}."

prompt=PromptTemplate(template=tmle)

user_tone=input("Enter the tone(formal/friendly/apologetic)")
receiver=input("Enter the mail id:")
user_topic=input("Enter the topic")
word=int(input("How many word:"))
sender=input("Enter the sender id:")

completed_prompt=prompt.invoke(
    {
        "tone":user_tone,
        "receiver":receiver,
        "topic":user_topic,
        "words":word,
        "sender":sender
    }
)

final_prompt=completed_prompt.text

llm=ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)

respose=llm.invoke(final_prompt)

print(respose.content)