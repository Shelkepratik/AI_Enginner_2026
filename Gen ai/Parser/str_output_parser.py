from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Create LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# Get response from LLM
response = llm.invoke("What is Python?")

# Create StrOutputParser object
parser_obj = StrOutputParser()

# Convert AIMessage into simple string
final = parser_obj.invoke(response)

# Print final output
print(final)