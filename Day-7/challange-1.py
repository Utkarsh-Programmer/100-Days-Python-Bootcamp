# Challenge 1
# Hangman Game.

import random

# list of words
word_list = ["ardvark", "baboon", "camel"]

# ------------------------------------------------------------------------------------------------------------------------------------------
# TODO Randomly choose a word from the 'word_list' and assign it to a variable called 'chosen_word'.
chosen_word = random.choice(word_list)

# TODO Ask the user to guess a letter and assign it to a variable called 'guess'. Make 'guess' lowercase.
guess = input("Guess a letter : ").lower()

# TODO Check of the letter guessed by the user is one of the letters in the 'chosen_word'.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
# ------------------------------------------------------------------------------------------------------------------------------------------
