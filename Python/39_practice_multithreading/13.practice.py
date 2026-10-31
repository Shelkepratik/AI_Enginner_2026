"""Write two functions, cook_rice() that sleeps for 3 seconds and cook_dal() that sleeps for 1 second, each printing a message when done. Start both threads and join both. Print the total time taken and write a comment on which one finished first and why."""


import threading
import time

def cook_rice():
    time.sleep(3)
    print("cooking the rice")

def cook_dal():
    time.sleep(1)
    print("cooking dal")

t1=threading.Thread(target=cook_rice,name="cook rice")
t2=threading.Thread(target=cook_dal,name="cook dal")

t1.start()
t2.start()

t1.join()
t2.join()
