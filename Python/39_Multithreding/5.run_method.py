from threading import Thread

class student(Thread):

    def run(self):#run() automatically called
        print("student name is","pratik")

t1=student()   

t1.start()
        
