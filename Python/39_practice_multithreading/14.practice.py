"""Using the functions from Q3, run them using the pattern start → join → start → join. Print the total time again and write a comment comparing it with the time from Q3"""


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
t1.join()

t2.start()
t2.join()

