from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_list = []

    def create(self):
        for square in range(4):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            self.paddle_list.append(new_square)
        spacing = 0
        for piece in self.paddle_list:
            piece.goto(spacing, 0)
            spacing += -20

    def up(self):
        self.paddle_list[0].setheading(90)

    def down(self):
        self.paddle_list[0].setheading(270)

