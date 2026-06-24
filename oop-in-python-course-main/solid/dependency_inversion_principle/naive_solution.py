# DIP BAD

# Engine is our "low-level" module
class Engine:
  def start(self):
    print("Engine started")

# An alternative engine class that is FASTER than the basic engine above!
class FastEngine(Engine):
  def start(self):
    print("Activated power boot!")
    print("Fast engine started")

# Car is our "high-level" module
class Car:
  def __init__(self):
    self.engine = Engine() # car is tightly-coupled to this particular engine. If we want to give it a FastEngine, then we have to MODIFY this class, breaking the open/closed principle.

  def start(self):
    self.engine.start() 
    print("Car started")

car = Car()
car.start()

# LOGS:
# Engine started
# Car started