from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing circle with radius {self.radius}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle with width {self.width} and height {self.height}")

class ShapeActions:
    def duplicate(self, shape):
        if isinstance(shape, Circle):
            copy = shape
            copy.radius = shape.radius
            copy.draw()
        elif isinstance(shape, Rectangle):
            copy = shape
            copy.width = shape.width
            copy.height = shape.height
            copy.draw()
        else:
            raise ValueError("Invalid shape provided")

# Example useage
shapeActions = ShapeActions()

# User adds a circle to GUI
circle = Circle(5)
circle.draw()  # Drawing circle with radius 5

# User adds a rectangle to GUI
rect = Rectangle(5, 10)
rect.draw()  # Drawing rectangle with width 5 and height 10

# User right-clicks the shapes and clicks "duplicate"
shapeActions.duplicate(circle)  # Drawing circle with radius 5
shapeActions.duplicate(rect)  # Drawing rectangle with width 5 and height 10
