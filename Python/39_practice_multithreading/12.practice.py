"""Create a thread named "ReportThread" for any simple function. Print its ident before calling start() and after calling start(). Write a comment explaining the difference."""

from threading import Thread,current_thread

def display():
    print("hello!")
    print("The thread name is:",current_thread().name)

t1=Thread(target=display,name="ReportThread")
print(current_thread().name)
print(t1.name)
print(current_thread().name)
print(t1.ident)
t1.start()
print(t1.ident)
