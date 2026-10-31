"""
5. Write a function send_message(name, text) that prints "Message to <name>: <text>". 
Create a thread for it using kwargs, passing the values in a dictionary."""


import threading

def send_message(name,text):
    print(f"meassage to {name}:{text}")

t1=threading.Thread(target=send_message,kwargs={"name":"pratik","text":"hii,how are you?"},name="send_message")

t1.start()