class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # making method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Max")
user_2 = User("002", "Tom")

user_1.follow(user_2)
print(
    f"{user_1.user_id}, {user_1.username}, {
        user_1.followers}, {user_1.following}"
)

print(
    f"{user_2.user_id}, {user_2.username}, {
        user_2.followers}, {user_1.following}"
)
