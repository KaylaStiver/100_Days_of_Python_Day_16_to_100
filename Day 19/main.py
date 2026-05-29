from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkeypress(key="w",fun=move_forwards)
screen.onkeypress(key="s",fun=move_back)
screen.onkeypress(key="a",fun=turn_left)
screen.onkeypress(key="d",fun=turn_right)
screen.onkeypress(key="c",fun=clear)
screen.exitonclick()