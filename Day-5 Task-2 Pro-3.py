class Account:
    def get_interest_rate(self):
        return 4


class SavingsAccount(Account):
    def get_interest_rate(self):
        return 6


class FixedDeposit(Account):
    def get_interest_rate(self):
        return 8


# Create objects of all three account types
a1 = Account()
a2 = SavingsAccount()
a3 = FixedDeposit()

# Put all objects in a list
accounts = [a1, a2, a3]

# Loop through the list
for account in accounts:
    print("Interest Rate:", account.get_interest_rate(), "%")