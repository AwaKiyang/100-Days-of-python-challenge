
from turtle import Turtle, Screen  # Import Turtle and Screen classes from turtle module
screen = Screen()  # Create a screen object for the game window
from random import randint  # Import randint for random number generation (not used in this code)

class Paddle:
    """
    Represents a paddle in a Pong game using the turtle graphics library.
    Attributes:
        paddle (Turtle): The turtle object representing the paddle.
    Methods:
        __init__():
            Initializes the Paddle object by creating a turtle with a square shape.
        paddles(x_axis):
            Configures the paddle's appearance and position.
            - Stretches the paddle's length to make it suitable for Pong.
            - Sets the resize mode to 'user' for custom sizing.
            - Colors the paddle white.
            - Lifts the pen to prevent drawing lines when moving.
            - Teleports the paddle to the specified x-axis position at y=0.
            - Sets the paddle's heading upwards (90 degrees).
        movement(move_up, move_down):
            Binds keyboard controls for moving the paddle up and down.
            - Defines an 'up' function to move the paddle upwards by 20 units, 
              ensuring it does not exceed the upper boundary (y <= 305).
            - Defines a 'down' function to move the paddle downwards by 20 units,
              ensuring it does not exceed the lower boundary (y >= -305).
            - Sets the movement speed to instant for responsive controls.
            - Binds the 'up' and 'down' functions to the specified keys.
            - Activates the screen's key listener to respond to keypress events.    
    """
    def __init__(self):
        self.paddle = Turtle(shape="square")  # Create a turtle object for the paddle

    def paddles(self, x_axis):
        self.paddle.shapesize(stretch_len=5)  # Stretch the paddle length
        self.paddle.resizemode("user")  # Set resize mode to user
        self.paddle.color("white")  # Set paddle color to white
        self.paddle.penup()  # Lift the pen to avoid drawing lines
        self.paddle.teleport(x=x_axis, y=0)  # Move paddle to specified x position, y=0
        self.paddle.setheading(90)  # Set paddle facing upwards

    def movement(self, move_up, move_down):
        def up():
            if self.paddle.ycor() <= 305:  # Check if paddle is within upper boundary
                self.paddle.speed(0)  # Set movement speed to instant
                self.paddle.setheading(90)  # Face upwards
                self.paddle.forward(20)  # Move paddle up by 20 units

        def down():
            if self.paddle.ycor() >= -305:  # Check if paddle is within lower boundary
                self.paddle.speed(0)  # Set movement speed to instant
                self.paddle.setheading(270)  # Face downwards
                self.paddle.forward(20)  # Move paddle down by 20 units

        screen.onkeypress(fun=up, key=move_up)  # Bind up movement to key
        screen.onkeypress(fun=down, key=move_down)  # Bind down movement to key
        screen.listen()  # Listen for keypress events


class Scoreboard:
    """
    A class to manage and display the scoreboard in a Pong game using the Turtle graphics library.
    Methods
    -------
    __init__():
        Initializes the Scoreboard by creating a Turtle object for rendering the score.
    total_score(score, aligment):
        Clears the previous score and displays the updated score at the top center of the screen.
        Parameters:
            score (int): The current score to display.
            aligment (str): The alignment of the score text (e.g., 'center', 'left', 'right').
    """
    def __init__(self):
        self.board = Turtle()  # Create a turtle object for the scoreboard

    def total_score(self, score, aligment):
        self.board.clear()  # Clear previous score
        self.board.hideturtle()  # Hide the turtle icon
        self.board.penup()  # Lift the pen to avoid drawing lines
        self.board.color("white")  # Set text color to white
        self.board.goto(0, 300)  # Move to top center of the screen
        self.board.write(f'  score : {score}  ', align=aligment, font=('Courier', 25, 'normal'))  # Display score

class Border:
    """
    Represents the border and middle court line for a Pong game using the Turtle graphics library.
    Methods
    -------
    __init__():
        Initializes the Border object and creates a Turtle instance for drawing.
    middle_court():
        Draws a vertical dashed line at the center of the screen to represent the middle court.
        The line is drawn from the top (y=350) to the bottom (y=-350) of the screen, with white color and a pen size of 5.
    """
    def __init__(self):
        self.border = Turtle()  # Create a turtle object for the border

    def middle_court(self):
        self.border.color('white')  # Set border color to white
        self.border.speed(0)  # Set drawing speed to instant
        self.border.penup()  # Lift the pen to avoid drawing lines
        self.border.teleport(x=0, y=350)  # Move to top center of the screen
        proceed = True  # Flag to control drawing loop
        while proceed == True:  # Loop to draw dashed line
            self.border.pendown()  # Lower pen to draw
            self.border.setheading(270)  # Face downwards
            self.border.pensize(5)  # Set pen size
            self.border.forward(20)  # Draw a segment
            self.border.penup()  # Lift pen to create gap
            self.border.forward(20)  # Move forward to next segment
            if self.border.ycor() <= -350:  # Check if reached bottom
                proceed = False  # Stop drawing

class Ball:
    """
    Represents a ball object in a Pong game using the Turtle graphics library.
    Attributes:
        ball (Turtle): The turtle object representing the ball, initialized with a circular shape and red color.
        x_move (int): The horizontal movement increment for the ball.
        y_move (int): The vertical movement increment for the ball.
    Methods:
        __init__():
            Initializes the ball with a circular shape, red color, and sets initial movement increments for both axes.
        ball_movement():
            Moves the ball to a new position based on its current coordinates and movement increments.
            The pen is lifted to prevent drawing lines, and the movement speed is set to instant.
        bouncey():
            Reverses the vertical direction of the ball by multiplying y_move by -1, simulating a bounce off a horizontal surface.
        bouncex():
            Reverses the horizontal direction of the ball by multiplying x_move by -1, simulating a bounce off a vertical surface.
    """
    def __init__(self):
        self.ball = Turtle(shape="circle")  # Create a turtle object for the ball
        self.ball.color("red")  # Set ball color to red
        self.x_move = 10  # Set initial x movement speed
        self.y_move = 10  # Set initial y movement speed

    def ball_movement(self):
        self.ball.penup()  # Lift the pen to avoid drawing lines
        self.ball.speed(0)  # Set movement speed to instant
        nex_x = self.ball.xcor() + self.x_move  # Calculate next x position
        nex_y = self.ball.ycor() + self.y_move  # Calculate next y position
        self.ball.goto(x=nex_x, y=nex_y)  # Move ball to new position

    def bouncey(self):
        self.y_move *= -1  # Reverse y direction for vertical bounce

    def bouncex(self):
        self.x_move *= -1  # Reverse x direction for horizontal bounce
