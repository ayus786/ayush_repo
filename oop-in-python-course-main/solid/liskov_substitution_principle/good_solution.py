from abc import ABC, abstractmethod

# Abstract Shape class
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width: float = 0.0, height: float = 0.0):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: float = 0.0):
        self.side = side

    def area(self):
        return self.side * self.side

# Example usage
rect = Rectangle()
rect.width = 5
rect.height = 10
print("Expected area = 10 * 5 = 50.")
print("Calculated area = " + str(rect.area()))

square = Square()
square.side = 5
print("Expected area = 5 * 5 = 25.")
print("Calculated area = " + str(square.area()))

# LOGS:
# Expected area = 10 * 5 = 50.
# Calculated area = 50

# Expected area = 5 * 5 = 25.
# Calculated area = 25
