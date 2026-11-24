class Wallet:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    @property
    def balance(self):
        return self.__balance


# Creating wallet object
w = Wallet(1000)

# Deposit money
w.deposit(500)

# Withdraw money
w.withdraw(200)

# Display current balance
print("Current balance:", w.balance)