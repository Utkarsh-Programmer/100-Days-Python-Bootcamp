# Dumb way to make a class.
""" class User:
    # 'def' keyword defines a function
    # '__init__'  is a reserved method name in Python which stands for initialize and is automatically called when a new object of the class is created.
    # 'self' parameter is a reference to the current instance of the class.
    def __init__(self):
        # prints when a new user is created.
        print("New user is being created.")


# making attributes
user_1 = User()
user_1.id = "001"
user_1.username = "Angela"

# accessing attributes
print(user_1.id)
print(user_1.username)


user_2 = User()
user_1.id = "002"
user_1.username = "Jack"

print(user_1.id)
print(user_1.username)
"""


# Better way to make a class
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "Max")
print(f"{user_1.user_id}, {user_1.username}, {user_1.followers}")

user_2 = User("002", "Tom")
print(f"{user_2.user_id}, {user_2.username}, {user_2.followers}")
