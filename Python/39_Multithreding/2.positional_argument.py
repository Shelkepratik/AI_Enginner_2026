from threading import Thread

def display(msg,times):
    for i in range(times):
        print(msg)

t1=Thread(target=display,args=("hello world",5),name="mythread")

t1.start()

print("Thr thread is:",t1.name)

print("The id is: ",t1.ident)

