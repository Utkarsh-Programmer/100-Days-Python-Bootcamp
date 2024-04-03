# Exercise 3
# Check whether the year is Leap or not.

# DON'T CHANGE THE CODE BELOW
year = int(input("Check the year : "))

# WRITE YOUR CODE HERE
# ------------------------------------------------------------------------------------------------------------------------------------------
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap.")
    else:
        print("Leap year.")
else:
    print("Not leap.")
# ------------------------------------------------------------------------------------------------------------------------------------------
