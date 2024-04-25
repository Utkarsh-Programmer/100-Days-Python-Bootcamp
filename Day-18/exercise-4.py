# Exercise 4
# Draw a random walk.

from turtle import Turtle, Screen
import random


# colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan",
          "magenta", "teal", "lime", "lavender", "brown", "black", "turquoise",
          "gold", "silver", "gray", "maroon", "navy"]

# angles to follow on
directions = [0, 90, 180, 270]

# Making Turtle
timmy = Turtle()
timmy.pensize(10)
timmy.speed(3)

# Random Walk
for _ in range(1000):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

# Making Screen
screen = Screen()
screen.exitonclick()
