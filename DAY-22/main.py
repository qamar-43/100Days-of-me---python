from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME!")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle =  Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "b")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    #detecting collisions of balls with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()



    #detct collision with ryt nd left padle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or  ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    #destect ryt paddle 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detection with left paddle
    if ball.xcor() > -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()