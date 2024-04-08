# Exercise 1
# Pain Area Calculator

# ------------------------------------------------------------------------------------------------------------------------------------------
# WRITE YOUR CODE HERE
import math


def paint_calc(height, width, cover):
    number_of_cans = (height*width)/cover
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")
# ------------------------------------------------------------------------------------------------------------------------------------------


# DONT'T CHANGE THE CODE BELOW
test_h = int(input("Height of the wall(m) : "))
test_w = int(input("Width of the wall(m) : "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
