from threading import Thread

def display():
   
    print("hello")

t1=Thread(target=display,name="display")
print("before start method:",t1.is_alive())
t1.start()
print("After start method:",t1.is_alive())
