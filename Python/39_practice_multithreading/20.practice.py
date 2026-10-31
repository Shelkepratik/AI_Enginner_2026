"""Write a function process_order(order_id) that sleeps for 1 second and prints "Order <order_id> processed by <thread name>". Create threads for order IDs 101, 102 and 103 using args. Start all of them, then print the active thread count, join all threads, and print the active thread count again."""

import threading
import time

def process_order(order_id):
    time.sleep(1)
    print(f"Order {order_id} processed by {threading.current_thread().name}")

# Create threads using args
t1 = threading.Thread(target=process_order, args=(101,), name="Order1")
t2 = threading.Thread(target=process_order, args=(102,), name="Order2")
t3 = threading.Thread(target=process_order, args=(103,), name="Order3")

# Start all threads
t1.start()
t2.start()
t3.start()

# Print active thread count
print("Active threads after starting:", threading.active_count())

# Join all threads
t1.join()
t2.join()
t3.join()

# Print active thread count again
print("Active threads after joining:", threading.active_count())
