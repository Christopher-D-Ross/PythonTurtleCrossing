from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


# This class will show the current level and game over if hit by a car.
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
