from threading import Thread

class student(Thread):#inherit the parent class

    def __init__(self,name):
        super().__init__()
        self.name=name
        print("coustructor called")

    def run(self):#run() automatically called
        print("student name is","pratik")

    def run(self):#run() automatically called
            print("student name is",self.name)

t1=student("om")   

t1.start()
        
