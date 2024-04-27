# Exercise 1
# Etch a sketch.


from turtle import Turtle, Screen

# making turtle
timmy = Turtle()


# turtle head position
current_heading = timmy.heading()


def up():
    """Moves turtle in upward direction."""
    timmy.forward(10)


def down():
    """Moves turtle in down direction."""
    timmy.backward(10)


def left():
    """Moves turtle in left direction."""
    timmy.left(20)


def right():
    """Moves turtle in right direction."""
    timmy.right(20)


# making screen
screen = Screen()

# listening events
screen.listen()
screen.onkey(key="w", fun=up)
screen.onkey(key="s", fun=down)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)

screen.exitonclick()
