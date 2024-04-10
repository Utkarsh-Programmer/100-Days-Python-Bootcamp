# Challenge 1
# Calculator Part 1.

# ------------------------------------------------------------------------------------------------------------------------------------------
import os
from logo import logo


def clear_terminal():
    """clears the terminal"""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')


def add(num1, num2):
    """add two numbers"""
    return num1+num2


def subtract(num1, num2):
    """subtract two numbers"""
    return num1-num2


def multiply(num1, num2):
    """multiply two numbers"""
    return num1*num2


def divide(num1, num2):
    """divide two numbers"""
    return num1/num2


# available operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    """performs the calculation."""

    # greeting
    print(logo)

    # first number
    num1 = int(input("Enter a number : "))

    is_on = True
    while is_on:
        # second number
        num2 = int(input("Enter a number : "))

        # display the available options
        for operation in operations:
            print(operation)

        # operation input
        operation_symbol = input("Pick an operation from the above : ")

        # answer
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # final output
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # if user wanna calculate more
        if input(f"\nType 'y' to continue calculating with {answer} or type 'n' to start a new calculation : ").lower() == "y":
            num1 = answer
        else:
            is_on = False
            clear_terminal()
            # Recursion : when a function calls itself.
            calculator()


calculator()
# ------------------------------------------------------------------------------------------------------------------------------------------
