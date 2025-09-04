from turtle import Turtle,Screen  # Import Turtle and Screen classes from turtle module
from random import randint  
import json      # Import randint function for random number generation

screen = Screen()                 # Create a Screen object for the game window

class Snake:                      # Define the Snake class

    def __init__(self):           # Constructor for Snake class
        self.snake_list = list()  # List to hold all snake segments
        self.spacing = 0          # Variable to manage spacing between segments
        self.food = Turtle(shape="circle")  # Create a Turtle object for food, shaped as a circle
        self.snake_food()         # Call method to place food on the screen

    def create_snake(self):       # Method to create initial snake body
        for snake in range(3):    # Loop to create 3 segments
            snake_body = Turtle(shape="square")  # Create a square-shaped Turtle for each segment
            snake_body.color('white')            # Set segment color to white
            snake_body.penup()                   # Lift pen to avoid drawing lines
            snake_body.goto(x = 0 + self.spacing, y=0)  # Position segment horizontally with spacing
            self.spacing-=20                     # Decrease spacing for next segment
            self.snake_list.append(snake_body)   # Add segment to snake list

    def add_segment(self):        # Method to add a new segment to the snake
        snake_body = Turtle(shape="square")      # Create a new square segment
        snake_body.color('white')                # Set color to white  
        snake_body.penup()                       # Lift pen
        last_body = self.snake_list[-1].pos()    # Get position of last segment
        snake_body.goto(last_body)               # Place new segment at last segment's position
        self.spacing-=20                         # Update spacing (not strictly needed here)
        self.snake_list.append(snake_body)       # Add new segment to snake list

    def move_snake(self):        # Method to move the snake forward
        for i in range(len(self.snake_list) -1,0,-1):  # Loop backwards through segments except head
            tp = self.snake_list[i-1].pos()            # Get position of previous segment
            self.snake_list[i].setpos(tp)              # Move current segment to previous segment's position
        self.snake_list[0].color("yellow")
        self.snake_list[0].forward(20)                 # Move the head forward by 20 units

    def control_snake(self):      # Method to control snake direction with keyboard
        def right():              # Function to turn right
            if self.snake_list[0].heading() != 180:    # Prevent reversing direction
                self.snake_list[0].setheading(0)       # Set heading to right (0 degrees)
        def up():                 # Function to turn up
            if self.snake_list[0].heading() != 270:    # Prevent reversing direction
                self.snake_list[0].setheading(90)      # Set heading to up (90 degrees)
        def left():               # Function to turn left
            if self.snake_list[0].heading() != 0:      # Prevent reversing direction
                self.snake_list[0].setheading(180)     # Set heading to left (180 degrees)
        def down():               # Function to turn down
            if self.snake_list[0].heading() != 90:     # Prevent reversing direction
                self.snake_list[0].setheading(270)     # Set heading to down (270 degrees)

        screen.onkey(right, "Right")   # Bind right arrow key to right function
        screen.onkey(up, "Up")         # Bind up arrow key to up function
        screen.onkey(left, "Left")     # Bind left arrow key to left function
        screen.onkey(down, "Down")     # Bind down arrow key to down function
        screen.listen()                # Listen for keyboard events

    def snake_food(self):              # Method to place food randomly on screen
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller
        self.food.color("red")         # Set food color to red
        self.food.penup()              # Lift pen to avoid drawing
        x = randint(-280,280)          # Generate random x position
        y = randint(-280,280)          # Generate random y position
        self.food.goto(x,y)            # Place food at random position


class Scoreboard:                      # Define Scoreboard class
    def __init__(self):                # Constructor for Scoreboard
        self.score_board = Turtle() 
        # Create a Turtle object for scoreboard

    def total_score(self,score):       # Method to display current score
        self.score_board.clear()       # Clear previous score
        self.score_board.hideturtle()  # Hide the turtle icon
        self.score_board.penup()       # Lift pen
        self.score_board.color("white")# Set text color to white
        self.score_board.goto(-150,270)   # Position score at top center
        self.score_board.write(f'  score : {score}   ',align='center', font=('Courier', 15, 'normal'))  # Write score
    
    def highestScore(self, highscore, new_score = ''):
        self.score_board.clear()       # Clear previous score
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score_board.goto(150,270)
        self.score_board.color("white")
        self.score_board.write(f'  {new_score} highscore : {highscore}',align='center', font=('Courier', 15, 'normal'))  # Write highscorescore
        

    def wall_collisoin(self,):          # Method to display game over on collision
        self.score_board.color("red")  # Set text color to red
        self.score_board.penup()       # Lift pen
        self.score_board.hideturtle()  # Hide turtle icon
        self.score_board.goto(0,0)     # Position text at center
        self.score_board.write(f'GAME OVER ',align='center', font=('Courier', 15, 'normal'))  # Write game over

class HighScore:
    def __init__(self):
        self.player_score = {"high_score" : 0}

    def saving_score(self):
        try:
            #saving as a json file
            with open('C:/Users/awaki/Desktop/100.py/day20/saved_score.json','w',encoding='utf-8') as f:  #create file if not exist
                json.dump(self.player_score,f,ensure_ascii=False,indent=4)  
            #ensure_ascii=False allows us to write non-ascii characters in the json file
        except FileNotFoundError:
            print("sorry wew could'nt locate the file saved_score.json")

    def reading_score(self):
        try:
            with open('C:/Users/awaki/Desktop/100.py/day20/saved_score.json',encoding="utf-8") as f:
                self.player_score = json.load(f)# json.load() reads the json file and transfers it's content 
        except FileNotFoundError:
            print("sorry we could no located file saved_score.json we are now creating it")
