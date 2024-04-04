# Exercise 3
# Adding Even Numbers.

# DON'T CHANGE THE CODE ABOVE
target = int(input("Enter a number between 0 to 1000 : "))

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
total = 0
for number in range(target+1):
    if number % 2 == 0:
        total += number

print(f"Sum of even numbers from 0 to {target} is {total}.")
# ------------------------------------------------------------------------------------------------------------------------------------------
