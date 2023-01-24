from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_left} : {self.score_right} ", align=ALIGNMENT, font=FONT)

