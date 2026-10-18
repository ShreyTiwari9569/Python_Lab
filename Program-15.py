from abc import ABC, abstractmethod
import math


# Abstract Base Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Vector class
class Vector(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    # Operator overloading for +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Operator overloading for ==
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Operator overloading for <
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"


# Main program
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print("Vector 1:", v1)
print("Vector 2:", v2)

# Addition
v3 = v1 + v2
print("Vector Addition:", v3)

# Equality
print("Are vectors equal?", v1 == v2)

# Comparison based on magnitude
print("Is Vector 1 smaller than Vector 2?", v1 < v2)

# Circle calculations
circle = Circle(5)
print("\nShape:", circle)
print("Circle Area:", round(circle.area(), 2))
print("Vector Magnitude:", v1.magnitude())