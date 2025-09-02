from turtle import Turtle,Screen           # Import Turtle and Screen classes from turtle module
from random import randint,choice          # Import randint and choice functions from random module
screen = Screen()                         # Create a screen object for the game

class CrossingTurtle:
    """
    Represents the player's turtle in a crossing game.
    This class encapsulates the creation and movement of a turtle object using the Turtle graphics library.
    The turtle starts at the bottom center of the screen and can be moved in four directions: up, left, right, and down.
    Attributes:
        turtle (Turtle): The turtle object representing the player.
    Methods:
        __init__():
            Initializes the CrossingTurtle instance by creating a turtle object,
            setting its shape, color, initial position, and orientation.
        fd():
            Moves the turtle forward (up) by 10 units. The turtle's heading is set to 90 degrees (upwards).
        left():
            Moves the turtle left by 10 units. The turtle's heading is set to 180 degrees (left).
        right():
            Moves the turtle right by 10 units. The turtle's heading is set to 0 degrees (right).
        down():
            Moves the turtle down by 10 units. The turtle's heading is set to 270 degrees (down).
    """
    def __init__(self):
        # Create the player's turtle and set its initial position and appearance
        self.turtle = Turtle(shape="turtle")   # Create a turtle object with 'turtle' shape
        self.turtle.penup()                    # Lift the pen to avoid drawing lines
        self.turtle.setheading(90)             # Set the turtle's facing direction to upwards (90 degrees)
        self.turtle.goto(0,-280)               # Move the turtle to starting position at bottom center
        self.turtle.color("black")             # Set the turtle's color to black

    def fd(self):
        # Move the turtle forward (up)
        self.turtle.setheading(90)             # Ensure the turtle is facing upwards
        self.turtle.forward(10)                # Move the turtle forward by 10 units

    def left(self):
        # Move the turtle left
        self.turtle.setheading(180)            # Set the turtle's direction to left (180 degrees)
        self.turtle.forward(10)                # Move the turtle forward by 10 units (left)

    def right(self):
        # Move the turtle right
        self.turtle.setheading(0)              # Set the turtle's direction to right (0 degrees)
        self.turtle.forward(10)                # Move the turtle forward by 10 units (right)

    def down(self):
        # Move the turtle down
        self.turtle.setheading(270)            # Set the turtle's direction to down (270 degrees)
        self.turtle.forward(10)                # Move the turtle forward by 10 units (down)

class Randomcars:
    """
    A class to manage the creation and storage of randomly generated car objects using the Turtle graphics library.
    Attributes
    ----------
    car_list : list
        A list to store the Turtle objects representing cars.
    chance : list of bool
        A list controlling the probability of car creation on each call to the cars() method.
    Methods
    -------
    __init__():
        Initializes the Randomcars instance, setting up the car list and chance list.
    cars():
        Randomly creates a car Turtle object based on the chance list. The car is assigned a random color,
        positioned at a random y-coordinate on the right edge of the screen, and added to car_list.
    """
    def __init__(self):  
        # List to store car turtles and chance list for car creation
        self.car_list = []                     # Initialize an empty list to store car objects
        self.chance = [True,False,False,False] # List to control probability of car creation

    def cars(self):
        # Randomly create a car based on chance
        if choice(self.chance) == True:        # Randomly decide whether to create a car
            car = Turtle(shape="square")       # Create a turtle object with 'square' shape for car
            car.shapesize(stretch_wid=1,stretch_len=2) # Stretch the car shape to make it rectangular
            colors = ["yellow","red","blue","pink","green","orange","purple","brown"] # List of possible car colors
            car.penup()                        # Lift the pen to avoid drawing lines
            car.setheading(180)                # Set car's direction to left (180 degrees)
            y_axis = randint(-260,260)         # Randomly choose a y-coordinate for car's position
            car.color(choice(colors))          # Randomly choose a color for the car
            car.teleport(x=300, y=y_axis)      # Move the car to the right edge at the chosen y-coordinate
            self.car_list.append(car)          # Add the car to the car list

class Scoreboard:
    """
    A class to manage and display the game scoreboard using a Turtle graphics object.
    Attributes
    ----------
    board : Turtle
        The Turtle object used to display the scoreboard and messages.
    Methods
    -------
    __init__():
        Initializes the Scoreboard by creating and hiding the Turtle object.
    total_Score(score):
        Clears the previous score and displays the current score at the top-left corner of the screen.
        Parameters
        ----------
        score : int
            The current score to display.
    game_over():
        Displays the 'GAME OVER' message at the center of the screen in red color.
    """
    def __init__(self):
        # Create the scoreboard turtle and hide it
        self.board = Turtle()                  # Create a turtle object for the scoreboard
        self.board.hideturtle()                # Hide the turtle icon

    def total_Score(self,score):
        # Display the current score on the screen
        self.board.clear()                     # Clear previous score display
        self.board.teleport(-250,250)          # Move the scoreboard to top left corner
        self.board.color("black")              # Set the scoreboard text color to black
        self.board.penup()                     # Lift the pen to avoid drawing lines
        self.board.write(f'SCORE : {score}', align="left", font=('Courier', 25, 'normal')) # Write the score

    def game_over(self):
        # Display 'GAME OVER' message
        self.board.color("red")                # Set the text color to red
        self.board.penup()                     # Lift the pen to avoid drawing lines
        self.board.teleport(0,0)               # Move the scoreboard to the center of the screen
        self.board.write(f'GAME OVER', align="center", font=('Courier', 25, 'normal')) # Write 'GAME OVER'
