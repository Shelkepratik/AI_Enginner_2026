
from pydantic import BaseModel
from typing import Optional


class Employee(BaseModel):
    # Define the schema
    name: str
    employee_id: Optional[str] = None
    age: int
    company: str = "TCS"


# Create Employee object
employee1 = Employee(
    name="Akshay",
    age=30
)

# Display employee details
print(employee1)
print(employee1.model_dump())