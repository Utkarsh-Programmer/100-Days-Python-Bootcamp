# Exercise 3
# Debug the code.

""" 
target = int(input("Enter a number : "))

for number in range(1, target+1):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
"""

# Solution
target = int(input("Enter a number : "))

for number in range(1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
