"""Create a list of five thread names ["T1", "T2", "T3", "T4", "T5"]. Using a for loop, create and start a thread for each name, where each thread prints its own name using threading.current_thread().name. Store the threads in a list and join all of them at the end, then print "All threads finished"."""

import threading

def display():
    print("Thread name:",threading.current_thread().name)

list1=["T1","T2","T3","T4","T5"]

threads=[]

for i in list1:
    t=threading.Thread(target=display,name=i)
    threads.append(t)
    t.start()


for t in threads:
    t.join()


print("All thread finished....")

