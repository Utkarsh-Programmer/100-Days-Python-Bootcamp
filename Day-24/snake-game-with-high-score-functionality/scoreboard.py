from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("Consolas", 24, "normal")


class Scoreboard(Turtle):
    """This class is responsible for managing scoreboard."""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Write score on the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=(FONT))

    def reset(self):
        """Sets high score and reset the previous score."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase score."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Shows the game over message."""
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALIGNMENT,
                   font=(FONT))
