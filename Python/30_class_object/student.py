class student:
    def __init__(self,name,age):
        print(id(self))
        self.name=name
        self.age=age
    def display(self):
        print("The name of student:",self.name)
        print("The age of student:",self.age)
s1=student("pratik",23)
print(id(s1))
print(s1.name)
print(s1.age)
s1.display()
