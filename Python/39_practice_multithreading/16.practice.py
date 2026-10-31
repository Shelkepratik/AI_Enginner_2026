"""Write a function make_payment() that sleeps for 2 seconds and prints "Payment done". Start it in a thread and, in the main program, use a while loop with is_alive() to keep printing "Processing payment..." every 0.5 seconds until the thread finishes."""

import threading
import time

def make_payment():
    time.sleep(2)
    print("payment Done")

t1=threading.Thread(target=make_payment,name="make payment")
t1.start()

while t1.is_alive():
    print("processing payment....")
    time.sleep(0.5)

print("print process complete")

