import turtle
import time
from turtle import Turtle

from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen=turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=ScoreBoard()

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_status=True


while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move(20)
    if snake.head.distance(food) < 20:
        food.refresh()
        score.detected()
        snake.extend()

    if  snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        game_status=False
        score.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            game_status=False
            score.game_over()





screen.exitonclick()