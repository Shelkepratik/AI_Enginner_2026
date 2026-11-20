from pydantic import BaseModel,Field,EmailStr
from typing import Optional


class Student(BaseModel):
    name:str=Field(min_length=3 ,max_length=20)
    roll_no:int
    marks:float=Field(ge=0,le=100)
    email:EmailStr
    city:str="Pune"
    phone:Optional[str]=None


name=input("Enter the name:")
roll_no=int(input("Enter the roll no:"))
marks=float(input("Enter the marks:"))
email=input("Enter the email")
city=input("Enter the city:")
phone=input("Enter the phone number:")

s=Student(name=name,roll_no=roll_no,marks=marks,email=email,city=city,phone=phone)

print("\n student Details:")
print(s)



