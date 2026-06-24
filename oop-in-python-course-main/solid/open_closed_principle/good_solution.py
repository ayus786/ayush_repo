from abc import ABC, abstractmethod
import math

# Abstract Shape class to define what methods each concrete shape class should implement
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.height * self.width

# Example useage
circle = Circle(10)
rectangle = Rectangle(5, 10)

print(f"Circle area: {circle.calculate_area()}")
print(f"Rectangle area: {rectangle.calculate_area()}")

# LOGS:
# Circle area: 314.1592653589793
# Rectangle area: 50
