# Challenge 4
# Hangman Game.

import random
from hangman_art import stages
from words import word_list
from logo import logo

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

# ------------------------------------------------------------------------------------------------------------------------------------------
# TODO Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' = 6.
lives = 6

# TODO If guess is not in the 'chosen_word', then reduce the 'lives' by 1. If 'lives' goes down to 0, then the game should end and user loses.

# game loop starts
game_on = True
while game_on:
    # user guess
    guess = input("Guess a letter : ").lower()

    # TODO If the user has already guessed the letter, then let them know.
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
        print("You Win!")

    # TODO Print the ascii art from the 'stages' that corresponds to the current number of lives the user has remaining.
    print(stages[lives])
# ------------------------------------------------------------------------------------------------------------------------------------------
