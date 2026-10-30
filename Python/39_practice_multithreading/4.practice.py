"""Write a function print_table(num) that prints the multiplication table of a number up to 10.
 Create two threads using args to print the table of 5 and the table of 8 at the same time."""

import threading
def print_table(num):
    for i in range(1,11):
        print(num, "*", i, "=", num * i)

# Create two child threads
t1=threading.Thread(target=print_table,args=(5,),name="print_table")
t2=threading.Thread(target=print_table,args=(8,),name="print_table")

t1.start()

t2.start()