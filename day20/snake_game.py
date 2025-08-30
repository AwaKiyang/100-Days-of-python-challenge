from turtle import Turtle,Screen
screen = Screen()
class Snake:

    def __init__(self):
        self.snake_list = list()
        self.spacing = 0

    def create_snake(self):
        for snake in range(3):
            snake_body = Turtle(shape="square")
            snake_body.color('white')
            snake_body.penup()
            snake_body.goto(x = 0 + self.spacing, y=0)
            self.spacing-=20
            self.snake_list.append(snake_body)

    def move_snake(self):
        for i in range(len(self.snake_list) -1,0,-1):
            tp = self.snake_list[i-1].pos()
            self.snake_list[i].setpos(tp) 

        self.snake_list[0].forward(20)

    def control_snake(self):
        def right():
            if self.snake_list[0].heading() != 180:
                self.snake_list[0].setheading(0)  
        def up():
            if self.snake_list[0].heading() != 270:
                self.snake_list[0].setheading(90)
        def left(): 
            if self.snake_list[0].heading() != 0:
                self.snake_list[0].setheading(180)
        def down():
            if self.snake_list[0].heading() != 90:
                self.snake_list[0].setheading(270)

        screen.onkey(right, "Right")
        screen.onkey(up, "Up")
        screen.onkey(left, "Left")
        screen.onkey(down, "Down")
        screen.listen() 