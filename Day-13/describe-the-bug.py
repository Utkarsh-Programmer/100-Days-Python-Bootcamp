# Describing the bug.
# On calling the function, the output should be the print statement but here, nothing prints in the console.

"""
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it.")


my_function()
"""


# Solution
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it.")


my_function()
