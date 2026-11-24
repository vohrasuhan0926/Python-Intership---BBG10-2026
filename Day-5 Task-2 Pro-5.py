class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Top Speed:", self.speed, "km/h")


# Create object
s1 = SportsCar("BMW", "M4 Competition", 250)

# Display information
s1.display_info()