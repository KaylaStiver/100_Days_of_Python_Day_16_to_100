import time
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.enemy_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-60, 220)
        self.write(self.enemy_score, align="center", font=("Courier", 40, "normal"))
        self.goto(0, 220)
        self.write("-", align="center", font=("Courier", 40, "normal"))
        self.goto(60, 220)
        self.write(self.user_score, align="center", font=("Courier", 40, "normal"))