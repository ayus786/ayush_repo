class Dog:
    def __init__(self,name,owner):
        self.name=name
        self.Owner=owner
    def bark(self):
        print(f"{self.name} barks bhau bhau and my owner is {self.Owner.get_name}. I live in {self.Owner.get_address()} and contact number is {self.Owner.get_contact_number()}")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name=name
        self.address=address
        self.contact_number=contact_number
    
    @property
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
    
    def get_contact_number(self):
        return self.contact_number

owner = Owner("Rahul","Pune",1234567890)
dog = Dog(name="Indie",owner=owner)
print(dog.name)
dog.bark()
