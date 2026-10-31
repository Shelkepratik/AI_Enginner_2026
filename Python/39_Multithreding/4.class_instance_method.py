from threading import Thread

class student:

    def display_info(self):
        print("student name is","pratik")

    @staticmethod
    def display_info2():
        print("student roll no is: ","B201")
        
obj1=student()

t1=Thread(target=obj1.display_info(),name="mythread1")

t2=Thread(target=student.display_info2(),name="mythread2")

t1.start()

t2.start()