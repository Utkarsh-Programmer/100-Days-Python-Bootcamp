# Exercise 2
# Banker Roulette (Select a random person from the names list to pay the bill.)

# DONT'T CHANGE THE CODE BELOW
import random

# this code converts the input into an array separating each name with a comma and a space.
names = input("Enter the names : ").split(", ")

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
number_of_people = len(names)
random_number = random.randint(0, number_of_people-1)
random_person = names[random_number]

print(f"{random_person} is going to pay the bill today.")
# ------------------------------------------------------------------------------------------------------------------------------------------
