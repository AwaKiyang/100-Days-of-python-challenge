from turtle import Turtle,Screen
from pong import Paddle,Border
import time
screen = Screen()
screen.setup(height=750, width=1400)
screen.bgcolor("black")
screen.title("MY PONG GAME")
screen.tracer(2)

border = Border()
border.middle_court()
paddle1 = Paddle()
paddle2 = Paddle()

paddle1.paddles(x_axis= -680)
paddle2.paddles(x_axis= 680)

screen.update()
time.sleep(1)

paddle1.movement(move_up="Up",move_down="Down")
paddle2.movement(move_up="w",move_down="s")

screen.exitonclick()

