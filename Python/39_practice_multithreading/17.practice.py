"""Create three threads named "Upload1", "Upload2" and "Upload3", each running a function that sleeps for 2 seconds. Print threading.enumerate() before starting any thread, after starting all three, and after joining all three."""

import threading
import time


def upload():
    time.sleep(2)
    print(threading.current_thread().name,"completed")

#create three thread

t1=threading.Thread(target=upload,name="upload1")
t2=threading.Thread(target=upload,name="upload2")
t3=threading.Thread(target=upload,name="upload3")

#Before starting any thread
print("Before starting:")
print(threading.enumerate())

#start all three thread
t1.start()
t2.start()
t3.start()

#after starting all thread
print("\nAfter starting:")
print(threading.enumerate())

#wait for all thread to finsih
t1.join()
t2.join()
t3.join()

#after joining all threads
print("\nAfter joining:")
print(threading.enumerate())




