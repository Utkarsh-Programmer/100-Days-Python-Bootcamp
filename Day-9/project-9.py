# Project 9
# Secret Auction.

# ------------------------------------------------------------------------------------------------------------------------------------------
import os
from logo import logo


# clear terminal
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')


# finding highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# greeting
print("Welcome to the secret auction program!")

# logo
print(logo)


# bids
bids = {}

# bid is not finished
bidding_finished = False

# auction runs till bidding is not finished
while not bidding_finished:
    # name and bid inputs
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    # if there are other bidders
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # clearing the terminal
        clear_terminal()
# ------------------------------------------------------------------------------------------------------------------------------------------
