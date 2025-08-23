    from turtle import Turtle,Screen
    screen = Screen()
    spacing = 0
    snake_list = list()



 # Move the snake segments from tail to head
    for i in range(len(snake_list) - 1, 0, -1):
        new_x = snake_list[i - 1].xcor()
        new_y = snake_list[i - 1].ycor()
        snake_list[i].setpos(new_x, new_y)

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