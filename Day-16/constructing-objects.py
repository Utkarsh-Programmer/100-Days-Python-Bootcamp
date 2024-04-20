# NOTE : class name should be in PascalCase.

import turtle

# making a timmy object from the 'Turtle' class, that comes from 'turtle' module.
timmy = turtle.Turtle()
print(timmy)

# shape() method changes the turtle shape.
timmy.shape("turtle")

# color() method changes the turtle color.
timmy.color("purple")

# forward() method moves turtle forward.
timmy.forward(100)

# making screen using turtle
screen = timmy.screen

# 'canvheight' attribute shows the height of the screen.
print(screen.canvheight)

# by using 'exitonclick()' method, screen only exits on mouse click.
screen.exitonclick()
