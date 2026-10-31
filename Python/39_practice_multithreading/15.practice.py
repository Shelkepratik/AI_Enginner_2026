"""Write a function long_task() that sleeps for 3 seconds. Create a thread for it and print is_alive() before start(), right after start(), and after join()."""


import threading
import time

def long_task():
    time.sleep(3)
    print("long task")

t1=threading.Thread(target=long_task,name="long task")
print("before the start():",t1.is_alive())
t1.start()
print("after the start():",t1.is_alive())

t1.join()
print("after the join():",t1.is_alive())

