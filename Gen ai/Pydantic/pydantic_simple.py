from pydantic import BaseModel


class Employee(BaseModel):
    #define the schema
    name:str
    employee_id:int
    age:int

#accepet the input for user
name=input("Enter the your name:")
employee_id=int(input("Enter your empolyee_id"))
age=int(input("Enter age:"))

employee1=Employee(name=name,employee_id=employee_id,age=age)

print(employee1)
