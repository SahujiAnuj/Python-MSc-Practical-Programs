# Program 23: BankAccount Class with Deposit and Withdrawal

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Holder : {self.owner}")
        print(f"Current Balance: {self.balance}")
        print("-----------------------")

# --- Main Program ---
# Creating an object
name = input("Enter Account Holder Name: ")
initial_amt = float(input("Enter Initial Deposit: "))

my_acc = BankAccount(name, initial_amt)

# Performing operations
my_acc.deposit(2000)
my_acc.withdraw(1500)

# Displaying result
my_acc.display()
