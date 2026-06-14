import asyncio
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.hideturtle()

    def create_car(self):
        rng = random.randint(1,6)
        if rng == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            start_y = random.randrange(-300, 300)
            car.goto(300,start_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        pass
