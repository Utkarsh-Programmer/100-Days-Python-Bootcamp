# Challenge 3
# Hangman Game.

import random

# list of words
word_list = ["ardvark", "baboon", "camel"]

# randomly chosen word
chosen_word = random.choice(word_list)

# adding blank "_" for each letter from the 'chosen_word'.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")

# ------------------------------------------------------------------------------------------------------------------------------------------
# TODO Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the 'chosen_word'. Then you can they they've won.
game_on = True
while game_on:
    guess = input("Guess a letter : ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)

    if "_" not in display:
        game_on = False
        print("You Win!")
# ------------------------------------------------------------------------------------------------------------------------------------------
