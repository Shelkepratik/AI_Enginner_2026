
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()


# Define Pydantic Schema
class Report(BaseModel):

    report_name: str = Field(
        description="Title of the report"
    )

    introduction: str = Field(
        description="Introduction about the topic, maximum 300 characters",
        max_length=300
    )

    causes: List[str] = Field(
        description="List of 2 to 5 causes",
        min_length=2,
        max_length=5
    )

    impact: List[str] = Field(
        description="List of 2 to 5 impacts",
        min_length=2,
        max_length=5
    )

    advantage: List[str] = Field(
        description="List of 2 to 5 advantages",
        min_length=2,
        max_length=5
    )

    disadvantage: List[str] = Field(
        description="List of 2 to 5 disadvantages",
        min_length=2,
        max_length=5
    )

    remedies: List[str] = Field(
        description="List of 2 to 5 remedies",
        min_length=2,
        max_length=5
    )

    conclusion: str = Field(
        description="A short conclusion about the topic, maximum 300 characters",
        max_length=300
    )


# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)


# Structured Output
structured_output_obj = llm.with_structured_output(Report)


# User Input
topic = input("Enter the topic: ")


# Prompt
prompt = f"""
Generate a report about {topic}.

You MUST generate ALL the following fields:

1. report_name
2. introduction
3. causes
4. impact
5. advantage
6. disadvantage
7. remedies
8. conclusion

Important:
- Do not skip any field.
- Introduction must be within 300 characters.
- Conclusion must be within 300 characters.
- Provide 2 to 5 points in every list.
- Follow the Pydantic schema exactly.
"""


# Invoke LLM
response = structured_output_obj.invoke(prompt)


# Display Output
print("\n-------- STRUCTURED REPORT --------")

print(response.model_dump())

print("\nReport Name:", response.report_name)
print("\nIntroduction:", response.introduction)

print("\nCauses:")
for item in response.causes:
    print("-", item)

print("\nImpacts:")
for item in response.impact:
    print("-", item)

print("\nAdvantages:")
for item in response.advantage:
    print("-", item)

print("\nDisadvantages:")
for item in response.disadvantage:
    print("-", item)

print("\nRemedies:")
for item in response.remedies:
    print("-", item)

print("\nConclusion:")
print(response.conclusion)
