from turtle import Turtle

# constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """This class is responsible for making and moving Turtle."""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("seagreen")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        """Moves the player up"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Moves player back to the starting position."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if the user successfully crosses."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
