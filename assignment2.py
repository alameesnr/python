# A simple USSD banking program

class USSD_Banking:
    def __init__(self):
        self.balance = 0  # Initial account balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance:.2f}")
        else:
            print("Invalid amount. Please try again.")

    def transfer(self):
        amount = float(input("Enter amount to transfer: "))
        if 0 < amount <= self.balance:
            recipient = input("Enter recipient account number: ")
            self.balance -= amount
            print(f"Transfer of {amount:.2f} to account {recipient} successful. New balance: {self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid amount. Please try again.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount:.2f} successful. New balance: {self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid amount. Please try again.")

    
            
            