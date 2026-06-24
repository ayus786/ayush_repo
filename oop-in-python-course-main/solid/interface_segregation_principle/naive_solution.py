# Interface segregation principle

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def volume(self):
        raise NotImplementedError("Volume not applicable for 2D shapes.")

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius**2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius**3)

# Example usage
circle = Circle(10)
print(f"Circle area: {circle.area()}")  # Should be: 314.1592653589793
print(
    f"Circle volume: {circle.volume()}"
)  # My text editor's linter flags no issue... but run the code and we get an exception -- circle has been forced to implement a method that it doesn't need

sphere = Sphere(10)
print(f"Sphere surface area: {sphere.area()}")  # Should be: 1256.6370614359173
print(f"Sphere volume: {sphere.volume()}")  # Should be: 4188.790204786391
