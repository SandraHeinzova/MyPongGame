from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("The Pong Game")
my_screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkeypress(right_paddle.up, "Up")
my_screen.onkeypress(right_paddle.down, "Down")
my_screen.onkeypress(left_paddle.up, "w")
my_screen.onkeypress(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

# collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.play_ball()

#  ball is out
    if ball.xcor() > 390:
        scoreboard.score_left += 1
        scoreboard.update_scoreboard()
        ball.reset_game()
    elif ball.xcor() < -390:
        scoreboard.score_right += 1
        scoreboard.update_scoreboard()
        ball.reset_game()


my_screen.exitonclick()
