from turtle import Turtle

class State_location:  # This class manages displaying state names and their positions on the map using Turtle graphics.
    """
    State_location class for displaying state names and game messages using Turtle graphics.
    Classes:
        State_location:
            Manages the display of state names at specified coordinates on a map and shows a 'GAME OVER' message.
            Methods:
                __init__():
                    Initializes the Turtle object for writing state names, hides the turtle icon, and lifts the pen to prevent drawing lines.
                set_location(x_cor, ycor, state_name):
                    Moves the Turtle to the specified (x_cor, ycor) coordinates and writes the given state_name at that position, centered, using Arial font size 8.
                game_over():
                    Displays a 'GAME OVER' message in red at the center of the screen using Courier font size 15.
    """
    def __init__(self):
        self.state_location = Turtle() # Create a new Turtle object for writing state names on the map.
        self.state_location.hideturtle() # Hide the turtle icon so only text appears, not the turtle shape.
        self.state_location.penup() # Lift the pen so the turtle moves without drawing lines.

    def set_location(self, x_cor, ycor, state_name):
        # Move the turtle to the specified x and y coordinates without drawing.
        self.state_location.teleport(x = x_cor, y = ycor)
        # Write the state name at the current turtle position, centered, with Arial font size 8.
        self.state_location.write(f'{state_name}', align="center", font=("Arial", 8, "normal"))

    def game_over(self,score): # This method displays a 'GAME OVER' message when the player makes a wrong guess.
        self.state_location.color("green") # Change the text color to red for emphasis.
        self.state_location.goto(0,0) # Move the turtle to the center of the screen.
        # Write 'GAME OVER' in the center, using Courier font size 15.
        self.state_location.write(f'GAME OVER YOUR SCORE IS : {score}', align='center', font=('Courier', 15, 'normal'))