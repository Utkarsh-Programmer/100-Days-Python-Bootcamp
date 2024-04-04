# Project 4
# Rock Paper Scissors.

# ------------------------------------------------------------------------------------------------------------------------------------------
import random

# greeting
print("Welcome to the Rock, Paper, Scissors Game!")

# user choice
user_choice = int(input("Make a choice:\n0, Rock\n1, Paper\n2, Scissors\n"))

# valid input check
if user_choice > 2:
    print("Invalid Input!")

else:
    # computer choice
    computer_choice = random.randint(0, 2)

    # choices made
    print(f"You Chose: {user_choice}")
    print(f"Computer Chose: {computer_choice}")

    # conditions
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer Wins!")
    elif user_choice < computer_choice:
        print("Computer Wins")
    else:
        print("You Win!")
# ------------------------------------------------------------------------------------------------------------------------------------------
