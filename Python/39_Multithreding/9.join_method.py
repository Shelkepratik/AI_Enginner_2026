"""join()=the join method is used to make main thread util the specified thread completes it's execution"""

from threading import Thread,current_thread
import threading
import time

def display1():
    time.sleep(4)
    print("this is display1 function executed by  thread1")
    #print("thread is executed by:",threading.get_ident())
    

def display2():
    print("this is display 2 function executed by thread 2")
    #print("This is executed by: ",threading.get_ident())
    

def display3():
    print("this is display3 function executed by mainthread")
    #print("the is executed by display 3:",threading.get_ident())

t1=Thread(target=display1,name="display1")
t2=Thread(target=display2,name="display2")

t1.start()
t1.join()
#print("name for thread1: ",t1.name)
#print("ID of thread1",t1.ident)

t2.start()
t2.join() #main thread execute after thread2 that time we use join() method
3#print("name for thread1: ",t2.name)
#print("ID of thread2:",t2.ident)

#print("the current thread is:",current_thread().name)
display3()#run for mainThread






