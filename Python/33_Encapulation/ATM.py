class ATM:
    def __init__(self):
        self.secret_pin=""
        self.__account_bal=5000

    def set_pin(self):
        self.secret_pin=input("Enter the secret pin:")

    def view_balance(self):
        print("account is:",self.__account_bal)

    def withdraw(self,amt):
        if self.secret_pin==input("Enter the pint:"):
            if self.__account_bal>amt:
                self.__account_bal=self.__account_bal-amt
                print("updated balance:",self.__account_bal)
            else:
                print("insufficient balance")
        else:
            print("incorrect balance")
obj1=ATM()
#obj1.account_bal=0#access the instance variable outside the class
#obj1.account_bal=0#donot access beacuse this variable is private
#obj1.__account_bal=0 #do not change the account_bal value
obj1.set_pin()
obj1.view_balance()
obj1.withdraw(500)
