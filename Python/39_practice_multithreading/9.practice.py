"""Create a class named Greeter that inherits from Thread. Its _init() should take a person's name, call super().init_(), and store the name. 
Its run() method should print "Hello, <name>". Create three Greeter objects with different names and start all three."""


from threading import Thread

class Greeter(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print("hello",self.name)

g=Greeter("pratik")
g2=Greeter("om")
g3=Greeter("ram")

g.start()
g2.start()
g3.start()

