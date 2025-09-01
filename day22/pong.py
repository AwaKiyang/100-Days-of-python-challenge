from turtle import Turtle,Screen
screen = Screen()
class Paddle:
    def __init__(self):
        self.y_axis = 20
        self.paddle_list = list()

    def paddles(self,x_axis):
        for i in range(4):
            paddle = Turtle(shape="square")
            paddle.color("white")
            paddle.penup()
            paddle.teleport(x= x_axis, y = self.y_axis)
            self.y_axis -= 20
            self.paddle_list.append(paddle)

    def movement(self,move_up,move_down):
        def up():
            if self.paddle_list[0].ycor() <= 355:
                for i in range(len(self.paddle_list) -1,-1,-1):  
                    self.paddle_list[1].speed(0)  
                    self.paddle_list[i].setheading(90)
                    self.paddle_list[i].forward(20)

        def down():
            if self.paddle_list[-1].ycor() >=- 355:
                for i in range(len(self.paddle_list)):
                    self.paddle_list[1].speed(0)  
                    self.paddle_list[i].setheading(270)
                    self.paddle_list[i].forward(20)
            
        screen.onkeypress(fun=up,key=move_up)
        screen.onkeypress(fun=down,key=move_down)
        screen.listen()


    
class Border:    
    def __init__(self):
        self.border = Turtle()

    def middle_court(self):
        self.border.color('white')
        self.border.speed(0)
        self.border.penup()
        self.border.teleport(x=0, y=375)
        proceed = True
        while proceed == True:
            self.border.pendown()
            self.border.setheading(270)
            self.border.pensize(5)
            self.border.forward(20)
            self.border.penup()
            self.border.forward(20)
            if self.border.ycor() <= -375:
                proceed = False
    

        