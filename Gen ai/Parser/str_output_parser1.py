
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)

# Create Prompt Template
prompt = PromptTemplate(
    template="Explain {topic} in simple language.",
    input_variables=["topic"]
)

# Create Output Parser
parser = StrOutputParser()

# Create Chain
chain = prompt | llm | parser

# User Input
topic = input("Enter the topic: ")

# Get Response
response = chain.invoke({"topic": topic})

# Print Output
print("\nResponse:")
print(response)
