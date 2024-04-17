# Fixing Errors.
# This code has a TypeError and bug in the print statement. Fix this problem.

""" age = input("How old are you? ")
if age > 18:
    print("You can drive at age {age}.")
"""

# Solution
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
