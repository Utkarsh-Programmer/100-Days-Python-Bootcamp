# Project 23
# Turtle Crossing Game.

# ------------------------------------------------------------------------------------------------------------------------------------------
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Making Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Making player
player = Player()

# Making Cars
car_manager = CarManager()

# Making Scoreboard
scoreboard = Scoreboard()

# Moving Player
screen.listen()
screen.onkeypress(player.up, "Up")

# Conditions when the game is on
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect Collision with Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Player Successfully Crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
# ------------------------------------------------------------------------------------------------------------------------------------------
