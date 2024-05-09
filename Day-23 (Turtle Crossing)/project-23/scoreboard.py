from turtle import Turtle
# constants
FONT = ("Consolas", 24, "normal")


class Scoreboard(Turtle):
    """This class is responsible for making and updating the scoreboard."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard after a level up."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level each time the turtle crosses."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Shows the game over message."""
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
