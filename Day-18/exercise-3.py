# Exercise 3
# Draw different shapes.

from turtle import Turtle, Screen
import random


def draw_shapes(sides):
    """Draw all shapes from triangle to decagon."""
    angle = 360/sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.left(angle)


# colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan",
          "magenta", "teal", "lime", "lavender", "brown", "black", "turquoise",
          "gold", "silver", "gray", "maroon", "navy"]

# Making Turtle
timmy = Turtle()
timmy.width(3)
timmy.speed("fast")


# Making Shapes
for num_sides in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shapes(num_sides)

# Making Screen
screen = Screen()
screen.exitonclick()
