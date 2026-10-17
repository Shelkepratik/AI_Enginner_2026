
class DigitalWallet:
    def __init__(self, owner_name, wallet_balance):
        self.owner_name = owner_name
        self.wallet_balance = wallet_balance

        while True:
            print("""
            1. Add Money
            2. Pay a Bill
            3. View Balance
            4. Exit
            """)

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_money()

            elif choice == "2":
                self.pay_bill()

            elif choice == "3":
                self.view_balance()

            elif choice == "4":
                print("Thank you for using Digital Wallet!")
                break

            else:
                print("Invalid choice!")

    def add_money(self):
        amount = int(input("Enter amount to add: "))

        if amount > 0:
            self.wallet_balance += amount
            print("Money added successfully!")
            print("New balance:", self.wallet_balance)
        else:
            print("Amount must be greater than zero!")

    def pay_bill(self):
        amount = int(input("Enter bill amount: "))

        if amount <= 0:
            print("Bill amount must be greater than zero!")

        elif amount <= self.wallet_balance:
            self.wallet_balance -= amount
            print("Bill paid successfully!")
            print("Remaining balance:", self.wallet_balance)

        else:
            print("Insufficient wallet balance!")

    def view_balance(self):
        print("Owner name:", self.owner_name)
        print("Wallet balance:", self.wallet_balance)


name = input("Enter owner name: ")
balance = int(input("Enter initial wallet balance: "))

wallet = DigitalWallet(name, balance)
