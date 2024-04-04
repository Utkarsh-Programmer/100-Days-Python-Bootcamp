# Random Module:
import random

# random number between 1 to 10.
random_integer = random.randint(1, 10)
print(random_integer)

# random floating point number between 0 to 1.
random_float = random.random()
print(random_float)

# random floating point number between 0 to 5.
random_float = random.random()*5
print(random_float)

# random love score
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")
