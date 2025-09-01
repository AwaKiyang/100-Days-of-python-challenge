from turtle import Turtle, Screen  # Import Turtle graphics classes
"""
This script implements a classic Pong game using the Turtle graphics library in Python.
Main Features:
--------------
- Sets up a game window with custom dimensions, background color, and title.
- Draws a middle court line using a custom Border class.
- Initializes two paddles (left and right) with custom positions and keyboard controls:
    - Left paddle: controlled by 'w' (up) and 's' (down).
    - Right paddle: controlled by 'Up' and 'Down' arrow keys.
- Creates a ball object that moves and bounces off paddles and top/bottom walls.
- Implements collision detection for ball and paddles, as well as scoring logic:
    - Ball bounces off paddles and walls.
    - When the ball passes the left or right edge, the respective player scores a point.
    - Scoreboards are updated for each player.
    - Ball resets to the center after each score.
- Uses manual screen updates for smooth animation.
- Game loop runs until the user closes the window.
- Exits the game when the user clicks on the screen.
Classes Used:
-------------
- Paddle: Handles paddle creation, positioning, and movement controls.
- Border: Draws the court border and middle line.
- Ball: Manages ball creation, movement, and bounce logic.
- Scoreboard: Displays and updates player scores.
Usage:
------
Run the script to start the Pong game. Control the left paddle with 'w' and 's', and the right paddle with the arrow keys. The game continues until the window is closed.
Note:
-----
Requires the 'pong' module containing Paddle, Border, Ball, and Scoreboard classes.
"""
from pong import Paddle, Border, Ball, Scoreboard  # Import custom game classes
import time  # Import time module for delays

screen = Screen()  # Create the game screen
screen.setup(height=700, width=1000)  # Set screen size
screen.bgcolor("black")  # Set background color
screen.title("MY PONG GAME")  # Set window title
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

border = Border()  # Create border object
border.middle_court()  # Draw the middle line on the court

left_paddle1 = Paddle()  # Create left paddle
rigth_paddle2 = Paddle()  # Create right paddle

left_paddle1.paddles(x_axis=-480)  # Position left paddle
rigth_paddle2.paddles(x_axis=480)  # Position right paddle

left_paddle1.movement(move_up="w", move_down="s")  # Set left paddle controls
rigth_paddle2.movement(move_up="Up", move_down="Down")  # Set right paddle controls

ball = Ball()  # Create ball object
left_board = Scoreboard()  # Create left scoreboard
right_board = Scoreboard()  # Create right scoreboard
left_score = 0  # Initialize left score
right_score = 0  # Initialize right score

proceed = True  # Game loop control variable
while proceed == True:  # Main game loop
    time.sleep(0.05)  # Pause for smooth animation
    screen.update()  # Update the screen
    ball.ball_movement()  # Move the ball

    # Bounce ball off top and bottom walls
    if ball.ball.ycor() > 330 or ball.ball.ycor() < -330:
        ball.bouncey()

    # Bounce ball off right paddle
    if ball.ball.distance(rigth_paddle2.paddle) < 50 and ball.ball.xcor() > 450:
        ball.bouncex()

    # Bounce ball off left paddle
    if ball.ball.distance(left_paddle1.paddle) < 50 and ball.ball.xcor() < -450:
        ball.bouncex()

    # Ball passes left edge, right player scores
    if ball.ball.xcor() < -500:
        left_score += 1  # Increment left score
        left_board.total_score(score=left_score, aligment="left")  # Update left scoreboard
        ball.ball.goto(0, 0)  # Reset ball position
        ball.bouncex()  # Change ball direction

    # Ball passes right edge, left player scores
    if ball.ball.xcor() > 500:
        right_score += 1  # Increment right score
        right_board.total_score(score=right_score, aligment="right")  # Update right scoreboard
        ball.ball.goto(0, 0)  # Reset ball position
        ball.bouncex()  # Change ball direction

screen.exitonclick()  # Wait for user to click to exit
