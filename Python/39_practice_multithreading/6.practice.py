"""Write a function countdown() that prints numbers from 5 to 1 with a 1-second gap.
 Run it in a thread and print "Main program finished" after starting the thread. 
Run the program once without join() and once with join() before the last print, and 
write a comment explaining the difference in the output order."""


import threading
import time

def countdown():
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)

t1=threading.Thread(target=countdown)

t1.start()

print("main program finished")


