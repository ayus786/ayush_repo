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
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def area(self) -> float:
        return self.width * self.height

# Square class inheriting from Rectangle (LSP violation)
class Square(Rectangle):
    def __init__(self, side: float = 0.0):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value: float):
        """Set both width and height to the same value."""
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value: float):
        """Set both height and width to the same value."""
        self._height = value
        self._width = value

# Example usage (LSP violation in action)
# rect = Rectangle()
# rect.width = 5
# rect.height = 10
# print("Expected area = 10 * 5 = 50.")
# print("Calculated area = " + str(rect.area()))

# LOGS:
# Expected area = 10 * 5 = 50.
# Calculated area = 50

# Substituting Rectangle with Square (LSP violation)
rect = Square()
rect.width = 5  # Setting width will also set height to 5
rect.height = 10  # Setting height will also set width to 10
print("Expected area = 5 * 5 = 25.")  # This is misleading!
print("Calculated area = " + str(rect.area()))  # Output: 100

# LOGS:
# Expected area = 5 * 5 = 25.
# Calculated area = 100
