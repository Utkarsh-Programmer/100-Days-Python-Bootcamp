# Project 14
# Higher-Lower Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
from game_data import data
from logo import logo, vs
import random
import os


def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')


def format_data(account):
    """This function formats the data into a printable format and return a formatted string."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."


def check_answer(guess, a_followers, b_followers):
    """This function takes user guess and followers count and return if they got right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# logo
print(logo)

# variables
score = 0
game_on = True
account_b = random.choice(data)


# making game repeatable
while game_on:
    # generating random account from the game data
    # # ...'account_b' become 'account_a' after each correct guess
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(account_a["follower_count"])
    print(account_b["follower_count"])

    # comparison message
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # user guess.
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    # getting follower count
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    # checking user guess
    is_correct = check_answer(guess, a_followers, b_followers)

    # clearing the screen
    clear_terminal()

    # feedback on user guess.
    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}.")
    else:
        game_on = False
        print(f"Sorry, that's wrong! Your final score is {score}.")
# ------------------------------------------------------------------------------------------------------------------------------------------
