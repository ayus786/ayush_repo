class User:
    # Static attribute to count all users
    user_count = 0

    def __init__(self, username, email):
        self.username = username  # Instance attribute
        self.email = email  # Instance attribute
        User.user_count += 1  # Increment the static attribute

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


# Creating user instances
user1 = User("dantheman", "dan@gmail.com")
user2 = User("sally123", "sally@gmail.com")

# Accessing instance attributes
print(user1.username)  # Output: dantheman
print(user2.username)  # Output: sally123

# Accessing static attribute
print(User.user_count)  # Output: 2
print(
    user1.user_count
)  # Output: 2 (but it's still shared, as this accesses User.user_count)
print(
    user2.user_count
)  # Output: 2 (but it's still shared, as this accesses User.user_count)
