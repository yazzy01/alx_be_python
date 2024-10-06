class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.1f}")  # Ensuring correct formatting
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")  # Ensuring correct formatting

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")  # Correctly format balance


# Example usage
def main():
    account = BankAccount(250)  # Initialize with a balance of $250
    account.deposit(67)          # Deposit $67
    account.withdraw(50)         # Withdraw $50
    account.withdraw(300)        # Attempt to withdraw more than the balance
    account.display_balance()     # Display the current balance

if __name__ == "__main__":
    main()

