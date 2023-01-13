from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("PONG")
#tracer turns off animation 0
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

player1_score = 0
player2_score = 0

game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # detect collision of ball with ceiling
  if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

  #detect collision with paddles
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
      ball.bounce_x()

  #detect if ball is missed by R paddle
  if ball.xcor() > 380:
    ball.reset_ball()
    scoreboard.l_point()

  # detect if ball is missed by L paddle
  if ball.xcor() < -380:
    ball.reset_ball()
    scoreboard.r_point()




screen.exitonclick()