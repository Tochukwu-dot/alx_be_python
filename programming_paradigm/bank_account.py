# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance with an optional initial balance (defaults to 0)."""
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient, otherwise deny withdrawal."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrawn: ${amount}")
            return True
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            return False
    
    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
