from turtle import Turtle, Screen
import random
# tim = Turtle()
screen = Screen()

#challenge 1
# def move_forwards():
#     tim.forward(10)
#
# def move_back():
#     tim.backward(10)
#
# def turn_right():
#     tim.right(10)
#
# def turn_left():
#     tim.left(10)
#
# def clear():
#     tim.home()
#     tim.clear()
#
# screen.listen()
# screen.onkeypress(key="w",fun=move_forwards)
# screen.onkeypress(key="s",fun=move_back)
# screen.onkeypress(key="a",fun=turn_left)
# screen.onkeypress(key="d",fun=turn_right)
# screen.onkeypress(key="c",fun=clear)


#challenge 2
game_continue = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtle_list = []

def generate_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    for shades in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(shades)
        new_turtle.penup()
        turtle_list.append(new_turtle)
    return turtle_list

def line_up_turtles(turtles):
    spacing = -70
    for t in turtles:
        t.goto(-230,spacing)
        spacing += 30

if user_bet:
    game_continue = True

generate_turtles()
line_up_turtles(turtle_list)

while game_continue:

    for turtle in turtle_list:
        distance = random.randint(1, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            winning_color = turtle.color()[0]
            print(f"The winning turtle is {winning_color}!")
            if winning_color != user_bet:
                print("You lose...")
            else:
                print("You win!")
            game_continue = False

screen.exitonclick()

