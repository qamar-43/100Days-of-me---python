from turtle import  Turtle ,Screen
from snake import Snake
import time
from food import Food
from score import Scoreboard


#importing turtle from turtle package nd from turtle importing screen nd giving it a "screen" as this is the syntax to be followed that wht ever  class we take froma apckage we need to name it which we call as object . nd each object has has its own functions which we callas attributes which can be used bu putting (.dot) as seen in code
screen = Screen()
screen.title("AI ANACONDA")
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#snake collisions with food
if snake.head.diatance(food) < 15:
    food.refresh()
    snake.extend()

#detect collisions with walll
if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
    game_is_on = False
    Scoreboard.game_over()


#detect collision with tail
#if heads collide with the tail trigger game_over
for segment in snake.segemnts[1: ]:
    if snake.head.diatnace() < 10:
        game_is_on = False
        scoreboard.game_over()
       

screen.exitonclick()