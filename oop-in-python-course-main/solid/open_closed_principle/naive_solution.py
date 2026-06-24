# Example violating O/CP. Let's also showcase Python's type hints in this example.

from enum import Enum
import math

class ShapeType(Enum):
    CIRCLE = "circle"
    RECTANGLE = "rectangle"

class Shape:
    def __init__(
        self,
        shape_type: ShapeType,
        radius: float = 0,
        height: float = 0,
        width: float = 0,
    ):
        self.type = shape_type
        self.radius = radius
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        # Warning: ugly stuff below 🤢🤮
        if self.type == ShapeType.CIRCLE:
            return math.pi * self.radius**2
        elif self.type == ShapeType.RECTANGLE:
            return self.height * self.width
        else:
            raise ValueError("Unsupported shape type.")

# Example usage
circle = Shape(ShapeType.CIRCLE, radius=5)
rectangle = Shape(ShapeType.RECTANGLE, height=4, width=6)

print(f"Circle Area: {circle.calculate_area()}")  # Circle Area: 78.53981633974483
print(f"Rectangle Area: {rectangle.calculate_area()}")  # Rectangle Area: 24
