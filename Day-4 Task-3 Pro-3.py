class InvalidAgeError(Exception):
    pass


def register_user(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be below 0.")
    elif age > 120:
        raise InvalidAgeError("Age cannot be above 120.")
    else:
        print("User registered successfully!")


try:
    register_user(150)

except InvalidAgeError as e:
    print("Error:", e)