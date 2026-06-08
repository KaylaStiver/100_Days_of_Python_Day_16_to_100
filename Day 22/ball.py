import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")

    def move(self):
        self.screen.update()
        time.sleep(0.1)
        self.goto(self.xcor() + 10, self.ycor() + 10)