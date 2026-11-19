
from typing import TypedDict, Annotated, Literal
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("openai_api_key"),
    temperature=0.7
)

# Define structured output
class ReviewAnalysis(TypedDict):
    summary: Annotated[
        str,
        "Provide summary in one line only"
    ]

    sentiment: Annotated[
        Literal["Positive", "Negative", "Neutral"],
        "Identify the sentiment of the review"
    ]


# Configure structured output
structured_output_obj = llm.with_structured_output(
    ReviewAnalysis
)

# Amazon product review
review = """
The Amazon app has become frustrating to use.
It frequently takes a long time to load product pages,
and sometimes the app crashes while making payments.
The user interface is confusing.
However, product delivery is fast and customer service
is helpful.
"""

# Generate structured response
response = structured_output_obj.invoke(
    f"Analyze the following Amazon app review:\n{review}"
)

# Display output
print("\nReview Analysis:")
print("Summary:", response["summary"])
print("Sentiment:", response["sentiment"])
print("Complete Response:", response)
