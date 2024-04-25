# Exercise 2
# Draw a dashed line.


from turtle import Turtle, Screen

# Making Turtle
timmy = Turtle()
timmy.color("coral")

# Making dashed line.
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

# Making Screen
screen = Screen()
screen.exitonclick()
