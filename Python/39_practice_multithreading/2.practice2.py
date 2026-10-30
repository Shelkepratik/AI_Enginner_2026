"""Write two functions, boil_water() and toast_bread(), each of which uses time.sleep(3) and then prints a message when done. 
First call them one after another and print the total time taken. 
Then run them using two threads and print the total time again. Write a comment comparing both times."""


from threading import Thread
import time

def boil_water():
    time.sleep(3)
    print("boiling the water")

def toast_bread():
    time.sleep(3)
    print("toast and bread")


print("without multithreading")
start=time.time()
boil_water()
toast_bread()
end=time.time()
print("without threading time:",end-start,"second")

print("with multithreading")
start=time.time()
t1=Thread(target=boil_water,name="boil_water")
t2=Thread(target=toast_bread,name="toast_bread")
t1.start()
t2.start()
t1.join()
t2.join()
end=time.time()
print("with threading time:",end-start,"second")
