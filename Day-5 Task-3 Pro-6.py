class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies cannot be compared")
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Different currencies cannot be compared")
        return self.amount > other.amount


m1 = Money(500, "INR")
m2 = Money(1000, "INR")
m3 = Money(700, "USD")

print("m1 < m2:", m1 < m2)
print("m2 > m1:", m2 > m1)

try:
    print("m1 > m3:", m1 > m3)
except ValueError as e:
    print("Error:", e)