from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_body = []
        self.screen = Screen()

        for snake in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            self.snake_body.append(new_segment)
        spacing = 0
        for segment in self.snake_body:
            segment.goto(spacing, 0)
            spacing += -20

    def move(self):
        self.screen.update()
        time.sleep(0.1)
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)



