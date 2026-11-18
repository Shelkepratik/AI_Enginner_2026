
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    huggingfacehub_api_token=os.getenv("hugging_face"),
    task="conversational",
    max_new_tokens=200,
    temperature=0.3
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is Generative AI?")

print(response.content)
