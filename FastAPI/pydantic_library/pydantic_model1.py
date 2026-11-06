from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int

Person1=Person(name="pratik",age="10")
"""pydantic autonatically convert string into interger"""

print(Person1.name)

print(Person1.age)