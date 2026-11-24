class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def display(self):
        print(f"{self.numerator}/{self.denominator}")


# Creating two fraction objects
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

# Adding two fractions using + operator
f3 = f1 + f2

print("First Fraction:")
f1.display()

print("Second Fraction:")
f2.display()

print("Addition of Fractions:")
f3.display()