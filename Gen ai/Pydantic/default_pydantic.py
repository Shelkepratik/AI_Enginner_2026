
from pydantic import BaseModel
from typing import Optional


class Employee(BaseModel):
    # Define the schema
    name: str
    employee_id: Optional[int] = None
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






# from pydantic import BaseModel


# class Employee(BaseModel):
#     # Define the schema
#     name: str
#     employee_id: int
#     age: int
#     company: str = "TCS"


# # Accept input from user
# name = input("Enter your name: ")
# employee_id = int(input("Enter your employee ID: "))
# age = int(input("Enter your age: "))
# company = input("Enter your company name (Press Enter for TCS): ")

# # Create Employee object
# if company:
#     employee1 = Employee(
#         name=name,
#         employee_id=employee_id,
#         age=age,
#         company=company
#     )
# else:
#     employee1 = Employee(
#         name=name,
#         employee_id=employee_id,
#         age=age
#     )

# # Display employee details
# print("\n----- Employee Details -----")
# print(employee1.model_dump())
