class BankATM:
    def __init__(self):
        self.secret_code=""
        self.account_bal=0
        self.show_menu()
    def show_menu(self):
        while True:
            choice=input('''
                        welcome! choose an option
                        1.create PIN
                        2.change PIN
                        3.check balance
                        4.withdraw cash
                        5.check information
                        6.Exit
                        Your choice is: 
                        ''')
            if choice=="1":
                self.set_pin()
            elif choice=="2":
                self.update_pin()
            elif choice=="3":
                self.check_balance()
            elif choice=="4":
                self.do_withdraw()
            elif choice=="5":
                self.display()
            elif choice=="6":
                self.Exit()
                break
            else:
                print("invalid choice!please try again")
                
            
      

    def set_pin(self):
        """set pin"""
        new_code=input("Enter the PIN:")
        self.secret_code=new_code
        #change the attribute value for new value
        #secret_code=""=>new_code="123"

        """opening_balance"""
        opening_balance=input("opening balance:")
        self.account_bal=int(opening_balance)
         #change the attribute value for new value
         #account_bal=0=>opening_balance=5000
        print("PIN created!")
        

    def update_pin(self):
        """change the pin"""
        current=input("Enter your current pin:")
        if current==self.secret_code:
            new_pin=input("Enter the new pin:")
            self.secret_code=new_pin
            print("pin updated!")
        else:
            print("enter pin not match")
        


    def check_balance(self):
        """check balance"""
        current_pin=input("provide your pin:")
        if current_pin==self.secret_code:
            print("Your Balance is:",self.account_bal)
        else:
            print("please!Enter correct pin to check account balance")
        

    def do_withdraw(self):
        """withdraw the money"""
        current_pin=input("Provide your pin:")
        if current_pin==self.secret_code:
            print("your balance is:",self.account_bal)
            amount=int("Enter amount to withdraw:")
            if amount<=self.amount_bal:
                self.account_bal=self.account_bal-amount
                print("New account balance:",self.account_bal)
            else:
                print("insufficient balance")
        else:
            print("wrong pin")
        
            
    def display(self):
        """Display user information"""
        print("The current pin code is:",self.secret_code)
        print("The current balance is:",self.account_bal)
        

    
    def Exit(self):
        print("Thank you")
        


obj1=BankATM()


