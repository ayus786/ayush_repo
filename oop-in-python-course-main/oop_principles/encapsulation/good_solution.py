# This class shows how we can use deposit and withdraw methods to perform validation before updating balance. BUT, it still allows balance to be modified directly. BankAccount2 solves this by introducing a property getter and omitting the property setter method.
class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

# Uncomment to test...
account = BankAccount()
print(account.balance)
# account.balance = -1
# print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)
account.withdraw(1)

# Problem: we can still modify the balance attr directly to a -ve number.

# Solution: add an underscore to balance attr to signify to clients that this is protected. In Python, a single underscore prefix (e.g., _balance) is a convention that indicates an attribute is protected, meaning it’s intended for internal use within the class or subclasses, but not enforced as private. It’s a hint to developers, not a strict rule.

class BankAccount2:
    def __init__(self):
        self._balance = 0.0

    # "Getter" property provides controlled access to _balance attr.
    @property
    def balance(self):
        return self._balance

    # If we don't provide a setter property, then _balance cannot be set directly outside of the class, providing safety against the balance being set to an invalid amount. To modify _balance, the provided deposit and withdraw api methods must be used.
    # @balance.setter
    # def balance(self, amount):
    #   self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount2()
print(account.balance)  # 0.0
# account.balance = -1 # This would give ERROR: Cannot assign to attribute "balance" for class "BankAccount"
account.deposit(1.99)
print(account.balance)  # 1.99
account.withdraw(1)
print(account.balance)  # 0.99
