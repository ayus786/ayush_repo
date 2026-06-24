# Everything that you create in Python is an object. Check this out:

name = "Danny"
age = 29

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>

# Objects are made by classes. Classes are the blueprints for objects, meaning they describe what an object should look like. So, above, let's look at the `name` variable:

# - The `name` variable is assigned to a string object
# - the `str` class defines what each string object looks like

# These classes demonstrate some of Python's "built-in" classes, that we can use to create data structures like strings and ints. But we can also create our own classes, then create objects (also known as instances) from those classes:

# Dog class describes what information ("attributes" or "data") and behaviours ("methods") every dog should have.
# First, lets create a very simple Dog class that has no data and just one behaviour
class Dog:
    def bark(self):
        print("Whoof whoof")

# # Define a variable called `dog` and assign it to an instance of (or "an object made from") the Dog class.
dog = Dog()
dog.bark()  # Whoof whoof

# Now let's add some data to the Dog class, so each dog object (or "instance") can have a name and a breed:
class Dog2:

    def __init__(self, first_name, last_name, breed):
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed

    def bark(self):
        print("Whoof whoof")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

# __init__ is a special method that is ran only once when an object is instanciated (created). We can setup our object data in here

scottyDog = Dog2("Angus", "Biggsby", "Scottish Terrier")
scottyDog.bark()
print(scottyDog.get_full_name())
print(scottyDog.breed)

houndDog = Dog2("Elvis", "Presley", "Basset Hound")
houndDog.bark()
print(houndDog.get_full_name())
print(houndDog.breed)

# Combining objects
class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

class Dog3:
    # __init__ is a special method that is ran only once when an object is instanciated (created). We can setup our object data in here
    def __init__(self, first_name, last_name, breed, owner):
        self.first_name = first_name
        self.last_name = last_name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")

    def get_full_name(self):
        return self.first_name + " " + self.last_name

owner = Owner("Danny", "122 Springfield Way, Uk", "8888 888 888")
scottyDog = Dog3("Bruce", "Biggs", "Scottish Terrier", owner)
print(scottyDog.owner.name)

# What is self?
# In Python, self is a special parameter that refers to the instance of the class (the object) you're working with. When you define a method within a class, the first parameter of that method is always self, by convention. This helps Python know that the method belongs to an instance of the class.

# Think of self as a way to refer to "this object" — the specific object that is calling the method. It gives each object its own set of attributes and allows access to methods that belong to it.

# Why Do We Need self?
# Without self, Python wouldn’t know which object you’re referring to when you use attributes or methods within a class. self ensures that each object can keep its own data separate and gives you a way to work with an object's attributes and methods.
