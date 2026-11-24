class Bird:
    def fly(self):
        print("Bird is flying with its wings.")


class Airplane:
    def fly(self):
        print("Airplane is flying using its engines.")


class Drone:
    def fly(self):
        print("Drone is flying using its propellers.")


# Function that accepts any object
def make_it_fly(obj):
    obj.fly()


# Create objects
b = Bird()
a = Airplane()
d = Drone()

# Call the same function with different objects
make_it_fly(b)
make_it_fly(a)
make_it_fly(d)