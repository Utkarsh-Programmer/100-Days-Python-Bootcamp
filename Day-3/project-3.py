# Project 3
# Treasure Island.

# ------------------------------------------------------------------------------------------------------------------------------------------
# greeting
print("Welcome to the Treasure Island!.\nYour mission is to find the Treasure.")

# conditions
move = input("Choose a direction, 'l' left or 'r' right : ").lower()
if move == "r":
    print("You lost in the jungle. Game Over!")

else:
    choice = input("Do you wanna, 's' swim or 'w' wait? ").lower()
    if choice == "s":
        print("You suffocated under water, You Died!")

    else:
        door = input(
            "Choose a door, 'r' red, 'y' yellow or 'b' blue : ").lower()
        if door == "y":
            print("You found the hidden Treasure. You Win!")
        else:
            print("You choice is bad, You Died!")
# ------------------------------------------------------------------------------------------------------------------------------------------
