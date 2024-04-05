# Challenge 2
# Hangman Game.

import random

# list of words
word_list = ["ardvark", "baboon", "camel"]

# randomly chosen word
chosen_word = random.choice(word_list)

# ------------------------------------------------------------------------------------------------------------------------------------------
# TODO Create an empty list called 'display'. For each letter in 'chosen_word', add a "_" to display.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")

# TODO Loop through each position in the 'chosen_word'. If letter at that position matches 'guess' then reveal the letter in the 'display' at that position.
guess = input("Guess a letter : ").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess

# TODO Print 'display' and you should see the guessed letter in the correct position and every other letter replaced with "_".
print(display)
# ------------------------------------------------------------------------------------------------------------------------------------------
