# Exercise 1
# Draw a square.

from turtle import Turtle, Screen

# Making Turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.pencolor("coral")

# Making Square
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

# Making Screen
screen = Screen()
screen.exitonclick()
