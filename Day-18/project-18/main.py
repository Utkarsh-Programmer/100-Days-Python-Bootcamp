# Project 18
# Hirst Painting.

# ------------------------------------------------------------------------------------------------------------------------------------------
import turtle
import random

# rgb colors in the image
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]


# making turtle
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# numbers of dots to make
number_of_dots = 100

# making dots with random colors
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # after 10 dots in a line, more dots will go in new line.
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


# making screen
screen = turtle.Screen()
screen.exitonclick()
# ------------------------------------------------------------------------------------------------------------------------------------------
