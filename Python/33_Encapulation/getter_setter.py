class ATM:
    def __init__(self):
        self.secrect_pin=""
        self.__account_bal=5000


    def set_pin(self):
        """set the pin"""
        self.secrect_pin=input("Enter your pin")



    def withdraw(self,amt:int):
        """withdraw the balance in the time of balanace is sufficient"""
        pin=input("Enter your pin:")
        if pin==self.secrect_pin:
            if self.__account_bal>amt:
                self.__account_bal=self.__account_bal-amt
                print("updated balance is:",self.__account_bal)
            else:
                print("Insufficient balance")
        else:
            print("please enter correct pin")

     #getter method
    def retrive_bal(self):
        """we access the amount"""
        return self.__account_bal

    #setter method
    def modify_bal(self,new_bal:int):
        """we modify the balance"""
        if type(new_bal)==int:
            self.__account_bal=new_bal
        else:
            print("invalid value")

    def deposit(self,value:int):
        pin=input("Enter the pin:")
        if self.secrect_pin==pin:
            if value>0:
                self.__account_bal=self.__account_bal+value
            else:
                print("zero and negative amount not added")
        else:
            print("incorrect pin so enter correct pin")

atm=ATM()
#print(atm.__account_bal)#not access
atm.modify_bal(10000)
atm.set_pin()
atm.withdraw(500)
print("after withdraw the amount:",atm.retrive_bal())
print(atm.deposit(1000))
print("after deposit the amount:",atm.retrive_bal())
