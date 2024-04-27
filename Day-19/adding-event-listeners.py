import turtle

# making turtle
timmy = turtle.Turtle()


def move_forward():
    """Moves turtle forward."""
    timmy.forward(10)


# making screen
screen = turtle.Screen()

# listens the event
screen.listen()

# adding event listener
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
