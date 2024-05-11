# Project 20-21
# Snake Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# making screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)  # turn off the turtle animations

# creating snake
snake = Snake()

# making food
food = Food()

# making scoreboard
scoreboard = Scoreboard()

# game is on
game_on = True

# moving snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# conditions when game is on
while game_on:
    screen.update()  # update screen
    time.sleep(.1)  # makes delay
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detecting collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()

# ------------------------------------------------------------------------------------------------------------------------------------------
