from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        y_cor = self.ycor()
        self.goto(self.xcor(), y_cor + 20)

    def move_down(self):
        y_cor = self.ycor()
        self.setpos(self.xcor(), y=y_cor - 20)

