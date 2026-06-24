from abc import ABC, abstractmethod
import math

class Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass

class Shape3D(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Circle(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius**2)

    def volume(self):
        return (4 / 3) * math.pi * (self.radius**3)

# Example usage
circle = Circle(10)
print(f"Circle area: {circle.area()}")  # Should be: 314.1592653589793
# print(f"Circle volume: {circle.volume()}")  # If uncomment this, linter now puts a squiggly line under `volume()` method, as if to say "circle's don't have volume, what are you doing?!"

sphere = Sphere(10)
print(f"Sphere surface area: {sphere.area()}")  # Should be: 1256.6370614359173
print(f"Sphere volume: {sphere.volume()}")  # Should be: 4188.790204786391
