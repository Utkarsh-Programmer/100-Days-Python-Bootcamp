# Project 7
# Hangman Game.

import random
from hangman_art import stages
from words import word_list
from logo import logo

# ------------------------------------------------------------------------------------------------------------------------------------------
# logo
print(logo)

# randomly chosen word
chosen_word = random.choice(word_list)
print(chosen_word)

# adding blank "_" for each letter from the 'chosen_word'.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")

# total lives
lives = 6

# game loop starts
game_on = True
while game_on:
    # user guess
    guess = input("Guess a letter : ").lower()

    # guess is already made
    if guess in display:
        print(f"You've already guessed {guess}.")

    # revealing the correct guessed letter in the 'display'
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    # checking if the guess is incorrect
    if guess not in chosen_word:
        print(f"You've guessed {guess}, which is not in the word.")
        lives -= 1
        # checking if lives are 0
        if lives == 0:
            game_on = False
            print("\nGame Over!")

    # game loop ends
    if "_" not in display:
        game_on = False
        print("\nYou Win!")

    # printing ascii art
    print(stages[lives])
# ------------------------------------------------------------------------------------------------------------------------------------------
