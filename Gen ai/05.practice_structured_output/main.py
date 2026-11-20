from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("openai_api_key"),
    temperature=0
)

class Recipe(BaseModel):
    dish_name: str = Field(min_length=3, max_length=30)
    cuisine: str
    cooking_time: int = Field(gt=0)
    ingredients: List[str]
    steps: List[str]
    is_vegetarian: bool

stuctured_llm=llm.with_structured_output(Recipe)

dish=input("Enter the dish name: ")

prompt=f"Give me a simple recipe for {dish}"

respose=stuctured_llm.invoke(prompt)

print("\nComplate Response:")
print(respose)

print("\nDish Name:",respose.dish_name)

print("Cooking Time:",respose.cooking_time,"min")

print("\n integredients:")
for integredients in respose.ingredients:
    print("-",integredients)

print("\ncooking steps:")
for step in respose.steps:
    print("-",step)

if respose.is_vegetarian:
    print("\nFood Type:veg")
else:
    print("\nFood Type:Non-veg")

print("\nJson output:")
print(respose.model_dump_json(indent=4))

