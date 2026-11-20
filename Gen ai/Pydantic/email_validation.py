from pydantic import BaseModel,EmailStr
from typing import Optional

class Employee(BaseModel):
    # Define the schema
    name: str
    employee_id: Optional[int] = None
    age: int
    company: str = "TCS"
    email:EmailStr


# Create Employee object
employee1 = Employee(
    name="Akshay",
    age=30,
    email="abc@gmail.com"
)

# Display employee details
print(employee1)





# from pydantic import BaseModel, Field

# class Employee(BaseModel):
#     name: str
#     email: str = Field(max_length=100)

# employee1 = Employee(
#     name="Pratik",
#     email="abc@gmail.com"
# )

# print(employee1)