""""Import the threading module and print the name and ident of the current thread. Write a comment explaining why the name is "MainThread"""

import threading

print("thee thread name:",threading.current_thread().name)
print("the id of this thread: ",threading.get_ident())