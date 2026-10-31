"""Create a class named Timer that inherits from Thread and overrides the run() method to print numbers from 1 to 3 with a 1-second gap. 
Create an object and start it using start().
 Then create another object and call run() directly, and print the current thread name inside run() in both cases. 
Write a comment explaining the difference."""

from threading import Thread,current_thread
import time

class Timer(Thread):
    def run(self):
        print("Thread name is:",current_thread().name)
        for i in range(1,4):
            print(i)
            time.sleep(1)

t=Timer()
t.start()
t.join()

print("------------------------------------")
t1=Timer()
t1.run()
        
