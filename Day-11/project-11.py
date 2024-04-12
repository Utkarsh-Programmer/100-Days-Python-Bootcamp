# Project 11
# Blackjack Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
import random
import os
from logo import logo


def clear_terminal():
    """This function clears the terminal"""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')


def deal_card():
    """Returns a random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # deck
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # change the value of ACE card from 11 to 1 if the sum of cards is greater than 21.
    if 11 in cards and sum(cards) > 21:
        # .remove() method removes the first occurrence of the specified element the list.
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares score for user and computer and return the result."""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You Lose!, Python has Blackjack."
    elif user_score == 0:
        return "You Win!, with a Blackjack."
    elif user_score > 21:
        return "You Lose!, you went over."
    elif computer_score > 21:
        return "You Win!, Python went over."
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"


def play_game():
    """This function contains logic to run the Blackjack Game."""
    # logo
    print(logo)
    # user cards and computer cards
    user_cards = []
    computer_cards = []

    # adding cards to user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # loops the game till it is not over
    game_over = False
    while not game_over:
        # user score and computer score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Python's first card: {computer_cards[0]}")

        # the way game overs
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            # another deal for user
            user_deal = input(
                "Type 'y' to get another card, type 'n' to pass : ").lower()

            # if user deals another card
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # after user plays the computer draws a cards till its score is less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Python's final hand: {
        computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# when user wanna play game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower() == "y":
    clear_terminal()
    play_game()
else:
    print("May be next time!")
# ------------------------------------------------------------------------------------------------------------------------------------------
