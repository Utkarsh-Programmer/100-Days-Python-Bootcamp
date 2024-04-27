# Project 19
# Turtle Race Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
from turtle import Turtle, Screen
import random

# turtle colors
colors = ["red", "goldenrod", "orangered", "darkblue", "green", "purple"]

# turtle y positions
y_pos = [-70, -40, -10, 20, 50, 80]

# all turtles
all_turtles = []

# race is off
race_on = False

# making screen
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("beige")
user_bet = screen.textinput(title="Make your bet.",
                            prompt="Which turtle will win the race? Enter a color: ")


# making 6 turtles and placing them at different positions and adding them in 'all_turtles' list.
for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

# race will be on if the user entered a input
if user_bet:
    race_on = True

# after race is on all turtle moves at a random pace
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle = turtle.pencolor()

            if winning_turtle == user_bet:
                print(f"You've Won! The winning turtle is {winning_turtle}.")
            else:
                print(f"You Lost! The winning turtle is {winning_turtle}.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()


# ------------------------------------------------------------------------------------------------------------------------------------------
