class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    account = BankAccount(250)  # Initialize with a starting balance
    account.deposit(67)          # Test deposit
    account.withdraw(50)         # Test withdrawal
    account.withdraw(300)        # Attempt to withdraw more than the balance
    account.display_balance()     # Check balance

