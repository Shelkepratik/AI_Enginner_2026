from pydantic import BaseModel, EmailStr
from typing import Optional

class Person(BaseModel):
    name: str = "rajesh"
    age: Optional[int] = None
    email: EmailStr


Person1 = Person(name="rahul", age=25, email="abc@gmail.com")

print(Person1.name)
print(Person1.age)
print(Person1.email)

# print(type(Person1.age))