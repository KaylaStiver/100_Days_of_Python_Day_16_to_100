from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")

game_continue = True

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

while game_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()


screen.exitonclick()