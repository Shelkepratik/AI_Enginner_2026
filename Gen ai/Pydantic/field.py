from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Employee(BaseModel):
    # Define the schema
    name: str=Field(min_length=3,max_length=20)
    employee_id: Optional[int] = None
    age: int=Field(gt=1,le=150,default=25,description="This age of employee")
    company: str = "TCS"
    email:EmailStr


# Create Employee object
employee1 = Employee(
    name="Akshay",
    #age=23
    email="abc@gmail.com"
)

# Display employee details
print(employee1)
