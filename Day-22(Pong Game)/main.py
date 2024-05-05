# Project 22
# Pong Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Making Paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Making Ball
ball = Ball()

# Making Scoreboard
scoreboard = Scoreboard()

# Screen Setup
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # turn of the animation

# Moving Paddles
screen.listen()
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")

# Updating Screen
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detecting Collision of ball with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detecting Collision of ball with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting left paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detecting right paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()
# ------------------------------------------------------------------------------------------------------------------------------------------
