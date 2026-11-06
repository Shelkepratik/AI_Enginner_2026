from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    name: str = "rajesh"
    age: Optional[int] = None

Person1 = Person(name="rahul", age=25)

Person2 = Person(name="rahul")

print(Person1.name)
print(Person1.age)

print(type(Person1.age))

print(Person2.name)
print(Person2.age)