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
color_list = ["MistyRose1", "plum", "SteelBlue", "pale goldenrod", "khaki", "LawnGreen"]
color_choice = random.choice(color_list)

for i in range(10):
    sides = 3
    arrow.color(color_choice)
    arrow.forward(100)
    arrow.left(360/sides)
    sides += 1


screen = Screen()
screen.exitonclick()