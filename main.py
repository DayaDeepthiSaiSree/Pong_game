from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from score_board import scoreboard
score_board = scoreboard()
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
# paddle.hideturtle()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)
game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or  ball.ycor() <= -280 :
        ball.bounce_y()
    if ball.xcor() > 380 :
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -380 :

        ball.reset_position()
        # ball.speed(10)
        score_board.r_point()

    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        ball.speed(10)

# if ball.xcor() == 280 or ball.ycor() == 200 or ball.xcor() == -280 or ball.ycor() == -280 :
#     ball.rand_move()

screen.exitonclick()