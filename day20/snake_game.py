from turtle import Turtle,Screen  # Import Turtle and Screen classes from turtle module
from random import randint  
import json      # Import randint function for random number generation

screen = Screen()                 # Create a Screen object for the game window

class Snake:                      # Define the Snake class
    """
    A class to represent the Snake in a classic Snake game using the turtle graphics library.
    Attributes
    ----------
    snake_list : list
        List of Turtle objects representing the segments of the snake's body.
    spacing : int
        Horizontal spacing used to position new segments when creating or adding to the snake.
    food : Turtle
        Turtle object representing the food that the snake eats.
    Methods
    -------
    __init__():
        Initializes the Snake object, creates the food Turtle, and places the food on the screen.
    create_snake():
        Creates the initial snake body with three segments, positions them horizontally, and adds them to snake_list.
    add_segment():
        Adds a new segment to the snake at the position of the last segment, extending the snake's length.
    move_snake():
        Moves the snake forward by updating each segment's position to follow the previous segment, and moves the head forward.
    control_snake():
        Sets up keyboard controls for the snake's direction (up, down, left, right), preventing reversal of direction.
    snake_food():
        Places the food Turtle at a random position on the screen, sets its color and size.
    """

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
    """
        A class to manage and display the score information for a Snake game using the Turtle graphics library.
        Attributes
        ----------
        score_board : Turtle
            The Turtle object used for rendering score and messages on the screen.
        Methods
        -------
        __init__():
            Initializes the Scoreboard by creating a Turtle object for score display.
        total_score(score):
            Clears the previous score and displays the current score at the top left of the screen.
        highestScore(highscore, new_score=''):
            Clears the previous score display and shows the high score at the top right of the screen.
            Optionally displays a new score alongside the high score.
        wall_collisoin():
            Displays a 'GAME OVER' message in red at the center of the screen when the snake collides with the wall.
    """
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
        # Clear previous score display
        self.score_board.clear()
        self.score_board.penup()        # Lift pen to avoid drawing lines
        self.score_board.hideturtle()   # Hide the turtle icon
        self.score_board.goto(150,270)  # Position high score at top right
        self.score_board.color("white") # Set text color to white
        # Display the high score and optionally the new score
        self.score_board.write(f'  {new_score} highscore : {highscore}', align='center', font=('Courier', 15, 'normal'))

    def wall_collisoin(self,):          # Method to display game over on collision
        self.score_board.color("red")   # Set text color to red
        self.score_board.penup()        # Lift pen to avoid drawing lines
        self.score_board.hideturtle()   # Hide turtle icon
        self.score_board.goto(0,0)      # Position text at center of screen
        # Display 'GAME OVER' message
        self.score_board.write(f'GAME OVER ', align='center', font=('Courier', 15, 'normal'))

class HighScore:
    """
    Manages the high score for a game by saving and loading the score from a JSON file.
    Attributes
    ----------
    player_score : dict
        Dictionary containing the high score with the key 'high_score'.
    Methods
    -------
    saving_score():
        Saves the current high score to a JSON file at the specified path.
        Handles file not found errors and prints a message if the file cannot be located.
    reading_score():
        Loads the high score from a JSON file at the specified path.
        Handles file not found errors and prints a message if the file cannot be located,
        and creates the file if it does not exist.
    """
    def __init__(self):
        # Initialize dictionary to store high score
        self.player_score = {"high_score" : 0}

    def saving_score(self):
        try:
            # Save high score as a JSON file
            with open('C:/Users/awaki/Desktop/100.py/day20/saved_score.json','w',encoding='utf-8') as f:
                # Write player_score dictionary to file with indentation for readability
                json.dump(self.player_score, f, ensure_ascii=False, indent=4)
                # ensure_ascii=False allows writing non-ASCII characters in the JSON file
        except FileNotFoundError:
            # Handle case where file path is invalid or inaccessible
            print("sorry we couldn't locate the file saved_score.json")

    def reading_score(self):
        try:
            # Read high score from JSON file
            with open('C:/Users/awaki/Desktop/100.py/day20/saved_score.json', encoding="utf-8") as f:
                # Load JSON content into player_score dictionary
                self.player_score = json.load(f)
        except FileNotFoundError:
            # Handle case where file does not exist and notify user
            print("sorry we could not locate file saved_score.json, we are now creating it")
