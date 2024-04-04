# Project 5
# Random Password Generator. (Easy)

# ------------------------------------------------------------------------------------------------------------------------------------------
import random

# greeting
print("Welcome to the PyPassword Generator!")

# letters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
           'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# symbols
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-"]

# user choice
letters_count = int(
    input("How many letters would you like in your password? "))
numbers_count = int(
    input("How many numbers would you like in your password? "))
symbols_count = int(
    input("How many symbols would you like in your password? "))

# final password
password = ""

# add letters
for _ in range(letters_count):
    random_letter = random.choice(letters)
    password += random_letter

# add numbers
for _ in range(numbers_count):
    random_number = random.choice(numbers)
    password += str(random_number)

# add symbols
for _ in range(symbols_count):
    random_symbol = random.choice(symbols)
    password += random_symbol

# final print statement
print(f"Your password could be {password}")
# ------------------------------------------------------------------------------------------------------------------------------------------
