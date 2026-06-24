from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def duplicate():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing circle with radius {self.radius}")

    def duplicate(self):
        newCircle = Circle(self.radius)
        return newCircle

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing rectangle with width {self.width} and height {self.height}")

    def duplicate(self):
        newRect = Rectangle(self.width, self.height)
        return newRect

class ShapeActions:
    def duplicate(self, shape):
        newShape = shape.duplicate()
        newShape.draw()

# Example useage
shapeActions = ShapeActions()

circle = Circle(5)
circle.draw()  # Drawing circle with radius 5

rect = Rectangle(5, 10)
rect.draw()  # Drawing rectangle with width 5 and height 10

shapeActions.duplicate(circle)  # Drawing circle with radius 5
shapeActions.duplicate(rect)  # Drawing rectangle with width 5 and height 10
