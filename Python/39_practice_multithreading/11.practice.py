"""1. Write a function check_stock() that prints "Checking stock" along with threading.current_thread().name and threading.get_ident(). Call it once directly from the main program and once using a thread named "StockThread". Write a comment comparing the two outputs.

"""
#from threading import current_thread
import threading

def check_stock():
    print("checking stock")
    print(threading.current_thread().name)
    print(threading.get_ident())

check_stock()
