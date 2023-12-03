from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0

    """Tracking the score after each successful crossing"""
    def level_up(self):
        self.clear()
        self.level += 1
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    """Player collided with a car"""
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

