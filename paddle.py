from turtle import Turtle

STEP = 15


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def up(self):
        y = self.ycor()
        if y < 240:
            self.sety(y + STEP)

    def down(self):
        y = self.ycor()
        if y > -240:
            self.sety(y - STEP)