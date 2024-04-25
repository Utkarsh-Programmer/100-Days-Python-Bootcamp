# Tuples:
# NOTE: Tuples cannot be modified.


# Making tuple.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))


# ------------------------------------------------------------------------------------------------------------------------------------------
# Modified Version of Exercise 4.
# NOTE: This version of exercise 4 can generate random RGB colors instead of some names colors.

import turtle
import random


def random_color():
    """Generates random RGB colors."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# angles to follow on
directions = [0, 90, 180, 270]

# Making Turtle
timmy = turtle.Turtle()
timmy.pensize(10)
timmy.speed(3)
turtle.colormode(255)

# Random Walk
for _ in range(1000):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

# Making Screen
screen = timmy.Screen()
screen.exitonclick()
