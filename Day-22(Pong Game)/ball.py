from turtle import Turtle


class Ball(Turtle):
    """This class is responsible for making ball and moving it."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        self.move()

    def move(self):
        """Moves the ball in the top right corner."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball on collision with wall in y axis."""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce the ball on collision with wall in x axis."""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """Reset the position of ball if the paddle misses the ball."""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
