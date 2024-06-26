from turtle import Turtle
import random


class Food(Turtle):
    """This class is responsible for generating food. """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("brown")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        """Refresh the food positions each time the snake collides."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
