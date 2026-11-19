
from typing import TypedDict
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


class ReportReview(TypedDict):
    Title: str
    Overview: str
    impact: str
    remedy: str


report = """Climate Change

Climate change refers to long-term changes in the Earth's
temperature and weather patterns. It is mainly caused by
human activities such as burning fossil fuels, deforestation,
and industrial pollution. It leads to global warming, melting
glaciers, rising sea levels, floods and droughts.
"""


load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0.7
)

structured_output_obj = llm.with_structured_output(ReportReview)

response = structured_output_obj.invoke(
    f"Analyze this report and provide the structured output:\n{report}"
)

print(response)
