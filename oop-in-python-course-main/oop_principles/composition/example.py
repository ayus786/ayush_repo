# Composition

# The "low-level" components that make up a car (the "high-level" component)
class Engine:
  def start(self):
    print("Starting engine")

class Wheels:
  def rotate(self):
    print("Rotate")

class Chassis:
  def support(self):
    print("Chassis supporting the car")

class Seats:
  def sit(self):
    print("Sitting on seats")

# Car is composed (made up from) of the above components
class Car:
    def __init__(self):
        # Private attributes (by convention, using a leading underscore) -- user of car doesn't want to think about all the low-level complexities ("implementation details") when starting the car. They just want to start and drive.
        self._engine = Engine()
        self._wheels = Wheels()
        self._chassis = Chassis()
        self._seats = Seats()

    def start(self):
        self._engine.start()
        self._wheels.rotate()
        self._chassis.support()
        self._seats.sit()
        print("Car started.")

car = Car()
car.start()