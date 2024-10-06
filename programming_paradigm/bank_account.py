class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

# Testing the class behavior
if __name__ == "__main__":
    account = BankAccount()
    account.deposit(67.0)
    account.withdraw(50.0)
    account.withdraw(100.0)
    account.display_balance()
