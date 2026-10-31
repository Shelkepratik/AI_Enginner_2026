from threading import Thread, active_count
import time

def display():
    time.sleep(2)
    print("Hello")

t1 = Thread(target=display, name="display")
t1.start()

print("Active threads:", active_count())

t1.join()

print("Active threads after join:", active_count())
