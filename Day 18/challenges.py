import turtle
from turtle import Turtle, Screen
import random

arrow = Turtle()

#challenge 1
# for i in range(4):
#     arrow.forward(100)
#     arrow.left(90)

#challenge 2
# for i in range(15):
#     arrow.forward(10)
#     arrow.up()
#     arrow.forward(10)
#     arrow.down()

#challenge 3
# color_list = ["MistyRose1", "plum", "SteelBlue", "pale goldenrod", "khaki", "LawnGreen"]
# color_choice = random.choice(color_list)
#
# sides = 3
# for i in range(3, 11):
#     arrow.color(color_choice)
#     for n in range(sides):
#         arrow.forward(100)
#         arrow.left(360 /sides)
#     sides += 1
#     color_choice = random.choice(color_list)

#challenge 4
# color_list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def randomize():
#     arrow.color(random.choice(color_list))
#     d = random.randrange(0, 360, 90)
#     return d
#
# arrow.pensize(10)
# arrow.speed(0)
#
# for steps in range(100):
#     degrees = randomize()
#     arrow.setheading(degrees)
#     arrow.forward(20)

#mini challenge
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# def randomize():
#     arrow.color(random_color())
#     d = random.randrange(0, 360, 90)
#     return d
#
# arrow.pensize(10)
# arrow.speed(0)
#
# for steps in range(100):
#     degrees = randomize()
#     arrow.setheading(degrees)
#     arrow.forward(20)

#challenge 5
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(100):
    arrow.speed(0)
    arrow.color(random_color())
    arrow.circle(100)
    arrow.left(5)

screen = Screen()
screen.exitonclick()