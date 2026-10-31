from threading import Thread

class MyClass(Thread):

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.result = None

    def run(self):
        self.result = self.a + self.b

t1 = MyClass(2, 3)

t1.start()

print(t1.result)