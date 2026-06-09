import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")


user_paddle = Paddle(350, 0)
enemy_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(enemy_paddle.up,"w")
screen.onkey(enemy_paddle.down,"s")
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down,"Down")

game_continue = True
while game_continue:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(user_paddle) < 50 and ball.xcor() > 340 or ball.distance(enemy_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.enemy_score += 1
        scoreboard.update_score()
        ball.home()
        ball.bounce_x()

    if ball.xcor() < -380:
        scoreboard.user_score += 1
        scoreboard.update_score()
        ball.home()
        ball.bounce_x()


screen.exitonclick()
