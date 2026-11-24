class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


# Creating point objects
p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(5, 15)

# Printing points
print("Point 1:", p1)
print("Point 2:", p2)
print("Point 3:", p3)

# Comparing points
print("Point 1 == Point 2:", p1 == p2)
print("Point 1 == Point 3:", p1 == p3)