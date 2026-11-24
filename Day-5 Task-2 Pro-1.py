class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)  # Initialize parent class attributes
        self.course = course

    def study(self):
        print(self.name, "is studying", self.course)


# Create Student object
s1 = Student("Suhan", 20, "Python")

s1.display()
print("Course:", s1.course)
s1.study()