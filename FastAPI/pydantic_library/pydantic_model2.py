from pydantic import BaseModel

class Person(BaseModel):
    name:str="ram"
    age:int="20"

Person1=Person(name="pratik",age=22)

Person2=Person()
#represent default value

print(Person1.name)

print(Person1.age)

print("use the default value")

print(Person2.name)

print(Person2.age)