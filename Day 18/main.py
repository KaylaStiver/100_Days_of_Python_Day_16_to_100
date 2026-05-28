import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
#
# rgb = []
# for color in colors:
#     rgb.append((color.rgb[0], color.rgb[1], color.rgb[2]))
#
# print(rgb)

arrow = Turtle()
turtle.colormode(255)

rgb = [(250, 228, 12), (198, 11, 36), (207, 13, 11), (233, 228, 5),
       (61, 205, 231), (247, 43, 12), (64, 25, 11), (112, 217, 109),
       (0, 130, 95), (141, 95, 173), (144, 219, 89), (255, 255, 255)]

def random_dot_line():
    for dot in range(10):
        current_color = random.choice(rgb)
        arrow.color(current_color)
        arrow.fillcolor(current_color)
        arrow.begin_fill()
        arrow.dot(20)
        arrow.end_fill()
        arrow.penup()
        arrow.forward(50)
        arrow.pendown()

for lines in range(10):
    arrow.speed(0)
    random_dot_line()
    arrow.teleport(0, arrow.ycor() + 50)


screen = Screen()
screen.screensize(2000,1500)
screen.exitonclick()