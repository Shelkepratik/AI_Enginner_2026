class AppUser:
    def __init__(self,username):
        self.username=username

    def login(self):
        print(self.username,"logged in!")

class student(AppUser):
    # def __init__(self,roll_no):
    #     self.roll_no=roll_no

    def enroll(self):
        print("enroll successfully")

student1=student("pratik")
student1.enroll()
student1.login()
        