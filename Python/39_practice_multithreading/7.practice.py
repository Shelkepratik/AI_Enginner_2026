"""7. Create a class Notifier with an instance method send_email() and a static method send_sms(), 
each of which prints a message. 
Create one thread with the instance method as the target and another with the static method as the target, and start both.
"""

from threading import Thread
class Notifier:
    def send_email(self):
        print("the person send the email")
    @staticmethod
    def send_sms():
        print("the send message")

n=Notifier()

t1=Thread(target=n.send_email(),name="send mail")
t2=Thread(target=Notifier.send_sms(),name="send message")

t1.start()
t2.start()
