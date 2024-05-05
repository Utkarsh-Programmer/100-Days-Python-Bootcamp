from turtle import Turtle


class Paddle(Turtle):
    """This class is responsible for making and moving the paddle."""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def up(self):
        """Moves paddle up."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves paddle down."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
