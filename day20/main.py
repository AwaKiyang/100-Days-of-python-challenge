from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)
snake_list = list()
spacing = 0
  
for snake in range(3):
    snake_body = Turtle(shape="square")
    snake_body.color('white')
    snake_body.penup()
    snake_body.goto(x = 0 + spacing, y=0)
    spacing-=20
    snake_list.append(snake_body)


proceed = True
while proceed == True:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snake_list) -1,0,-1):
        tp = snake_list[i-1].pos()
        snake_list[i].setpos(tp) 


    snake_list[0].forward(20)
    def right():
        snake_list[0].setheading(0)
    def up():
        snake_list[0].setheading(90)
    def left():
        snake_list[0].setheading(180)
    def down():
        snake_list[0].setheading(270)

    screen.onkey(right, "Right")
    screen.onkey(up, "Up")
    screen.onkey(left, "Left")
    screen.onkey(down, "Down")
    screen.listen() 
        
screen.exitonclick()
