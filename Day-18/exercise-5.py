# Exercise 5
#  Draw a Spirograph.


import turtle
import random


def random_color():
    """Generates random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# Making turtle
timmy = turtle.Turtle()
timmy.speed("fastest")
turtle.colormode(255)


# Making spirograph
def draw_spirograph(gap_size):
    """Draws a spirograph pattern."""
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)


draw_spirograph(5)

# Making screen
screen = turtle.Screen()
screen.exitonclick()
