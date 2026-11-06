from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Person(BaseModel):
    name: str = Field(min_length=3,max_length=20)
    age: Optional[int] = None
    email: EmailStr
    cgpa:float=Field(
        ge=0,#grater than
        lt=11,#less than
        default=5.0,
        description="cgpa of student"
    )


# Person1 = Person(name="rahul", age=25, email="abc@gmail.com",cgpa=-18.1)
Person1 = Person(name="rahul", age=25, email="abc@gmail.com",cgpa=8.1)

print(Person1.name)
print(Person1.age)
print(Person1.email)
print(Person1.cgpa)

# print(type(Person1.age))