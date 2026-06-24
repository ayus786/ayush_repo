from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

# Engine is our "low-level" module
class BasicEngine(Engine):
    def start(self):
        print("Basic engine started")

# We can now create different types of engines and inject them into car via dependency injection
class FastEngine(Engine):
    def start(self):
        print("Activated power boot!")
        print("Fast engine started")

# Car is our "high-level" module
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car started")

fastEngine = FastEngine()  # concrete implementation to be "injected" into the car
car = Car(
    fastEngine
)  # we can now inject any class that inherits the abstract Engine class, making our code more flexible because it is no longer tightly coupled to a particular concrete engine.
car.start()

# LOGS:
# Activated power boot!
# Engine started
# Car started
