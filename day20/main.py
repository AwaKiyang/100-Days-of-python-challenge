from turtle import Turtle,Screen
from snake_game import Snake
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)
snake = Snake()


snake.create_snake()
proceed = True
while proceed == True:
    screen.update()
    time.sleep(0.15)
    snake.move_snake()
    snake.control_snake()    


screen.exitonclick()

