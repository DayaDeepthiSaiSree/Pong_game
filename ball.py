from turtle import Turtle,Screen
import random
screen = Screen()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)
        self.screen.delay(50)
        # self.delay(50)
        self.goto(0,0)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        # self.screen.update()
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
        # self.speed(10)

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()