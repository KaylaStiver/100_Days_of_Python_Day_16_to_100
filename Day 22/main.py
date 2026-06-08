from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")


user_paddle = Paddle(-350, 0)
enemy_paddle = Paddle(350, 0)
ball = Ball()

screen.listen()
screen.onkey(enemy_paddle.up, "Up")
screen.onkey(enemy_paddle.down,"Down")
screen.onkey(user_paddle.up, "w")
screen.onkey(user_paddle.down,"s")

game_continue = True
while game_continue:
    screen.update()
    ball.move()

screen.exitonclick()
