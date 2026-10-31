"""Using the threads from Q7, print threading.active_count() at the same three points. Write a comment explaining why the count is 1 before starting the threads."""

import threading
import time

def upload():
    time.sleep(2)
    print(threading.current_thread().name, "completed")

# Create three threads
t1 = threading.Thread(target=upload, name="Upload1")
t2 = threading.Thread(target=upload, name="Upload2")
t3 = threading.Thread(target=upload, name="Upload3")

# Before starting any thread
print("Before starting:", threading.active_count())

# Start all three threads
t1.start()
t2.start()
t3.start()

# After starting all threads
print("After starting:", threading.active_count())

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

# After joining all threads
print("After joining:", threading.active_count())
