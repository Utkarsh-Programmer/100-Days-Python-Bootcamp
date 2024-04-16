# Project 12
# Number Guessing Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
import random


def greeting():
    """This function greets the user and prints a welcome message."""
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 to 100.")


def get_difficulty():
    """This function asks user to select a difficulty level."""
    return input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()


def get_win_number():
    """This function return the winning number for the Number Guessing Game."""
    return random.randint(1, 100)


def get_guess():
    """This function asks user to guess the number."""
    return int(input("Guess the number : "))


def play_game(difficulty):
    """This function is responsible to play the game. """
    win_number = get_win_number()

    # determine the total chances based on the chosen difficulty
    if difficulty == "easy":
        total_chances = 5
    elif difficulty == "hard":
        total_chances = 10
    else:
        print("Invalid Input!")
        return

    current_chances = 0

    # main game loop
    while total_chances > 0:
        guess = get_guess()
        current_chances += 1

        # compare the user's guess with the winning number
        if guess > win_number:
            total_chances -= 1
            print("Too High!")
            print(f"You have {
                  total_chances} chances left to guess the number.")
        elif guess < win_number:
            total_chances -= 1
            print("Too Low!")
            print(f"You have {
                  total_chances} chances left to guess the number.")
        else:
            print(f"You guessed the number {
                  current_chances} chances. You Win!")
            return

    print("You are out of chances. You Lose!")


def main():
    """This function is the entry point for the game."""
    greeting()
    play_game(get_difficulty())


# program runs if the script is executed directly by the Python Interpreter and not imported as a module in another script.
if __name__ == "__main__":
    main()
