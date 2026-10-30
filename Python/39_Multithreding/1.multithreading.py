from threading import Thread
import time

def addition():
    time.sleep(10)
    num1=10
    num2=20
    result=num1+num2
    print(result)
   

def multiplication():
    time.sleep(10)
    num1=10
    num2=20
    result=num1*num2
    print(result)
    

def division():
    time.sleep(10)
    num1=10
    num2=20
    result=num2/num1
    print(result)
    
t1=Thread(target=addition,name="mythread1")
t2=Thread(target=multiplication,name="mythread2")
t3=Thread(target=division,name="mythread3")

start=time.time()
t1.start()
t2.start()
t3.start()
end=time.time()

t1.join()
t2.join()
t3.join()
