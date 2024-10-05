# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount to the account and print the amount deposited."""
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")  # Ensure only one print statement

    def withdraw(self, amount):
    
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")  # Ensure only one print statement
            return True
        else:
            print("Insufficient funds.")  # Simplified to only print the required message
            return False

    def display_balance(self):
        """Display the current balance in the account."""
        print(f"Current Balance: ${self.account_balance:.2f}")  # Print the current balance
