class InvalidNumberError(Exception):
    pass

while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))

        if num < 1 or num > 10:
            raise InvalidNumberError("Number must be between 1 and 10.")

        print("Valid number:", num)
        break

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

    except InvalidNumberError as e:
        print(e)