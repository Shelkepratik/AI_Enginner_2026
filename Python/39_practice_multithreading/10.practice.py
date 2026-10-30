"""Create a class named SquareCalculator that inherits from Thread.
 Its _init_() should take a number, and its run() method should store the square of the number in self.result. 
 Create two objects for 12 and 25, 
start both, and use join() before printing both results so that the correct values (not None) are printed."""

from threading import Thread

class squarecalculator(Thread):
    def __init__(self,num):
        super().__init__()
        self.num=num
        self.result=None

    def run(self):
        self.result = self.num ** 2

s1=squarecalculator(12)
s2=squarecalculator(25)
s1.start()
s2.start()
s1.join()
s2.join()


# Print results
print("Square of 12:", s1.result)
print("Square of 25:", s2.result)