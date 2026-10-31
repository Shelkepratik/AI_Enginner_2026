from threading import Thread, enumerate
import time

def display():
    time.sleep(2)
    print("Hello")

t1 = Thread(target=display, name="display")
t1.start()

threads = enumerate()

for t in threads:
    print("Thread name:", t.name)

t1.join()
