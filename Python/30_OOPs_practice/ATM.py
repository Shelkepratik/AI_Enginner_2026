class ATM:
    def __init__(self):
        self.pin=""
        self.amount=0
        
        while True:
            print("""
                    1.create pin 
                    2.change pin
                    3.check balance
                    4.withdraw cash
                    5.exit
                     """)
            try:
                choice=int(input("Enter the number:"))
            except ValueError as err:
                print("only accept the value")
                continue
            if choice==1:
                self.create_pin()
            elif choice==2:
                self.change_pin()
            elif choice==3:
                self.check_balance()
            elif choice==4:
                self.withdraw_cash()
            elif choice==5:
                break
            else:
                print("Invalid choice")

    def create_pin(self):
        while True:
            new_pin = input("Enter the PIN: ")
            if new_pin.isalnum() and len(new_pin) == 8:
                self.pin = new_pin
                print("PIN created successfully!")
                break
            else:
                print("PIN must contain exactly 4 digits!")

        """opening balance"""
        openning_balance=int(input("Enter the amount:"))
        self.amount=openning_balance


    def change_pin(self):
        current_pin=input("Enter the old pin")
        if current_pin==self.pin:
            new_pin=input("Enter the new pin")
            if new_pin.isalnum and len(new_pin)==8:
                self.pin=new_pin
                print("pin update successfully")
            else:
                print("PIN must be alphnumeric and pin contain only 8 character")
        else:
            print("pin not match")


    def check_balance(self):
        securty_pin=input("Enter the your pin")
        if securty_pin==self.pin:
            print("The your current balance is:",self.amount)
        else:
            print("your securty pin not correct!")

    def withdraw_cash(self):
        securty_pin=input("Enter the your pin:")
        if self.pin==securty_pin and self.pin!="":
            withdraw_amount=int(input("Enter the amount:"))
            if withdraw_amount<=self.amount:
                self.amount=self.amount-withdraw_amount
                print("your remmaning amount is:",self.amount)
            else:
                print("please you are do not withdraw money")
        else:
            print("securty pin is incorrect!")

atm=ATM()