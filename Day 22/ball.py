import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xdiff = 10
        self.ydiff = 10
        self.speed = 0.01


    def move(self):
        self.screen.update()
        time.sleep(0.1)
        self.goto(self.xcor() + self.xdiff, self.ycor() + self.ydiff)

    def bounce_y(self):
        self.ydiff *= -1

    def bounce_x(self):
        self.xdiff *= -1
        self.speed *= 0.9

