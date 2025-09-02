
"""
This module implements the main loop for the Turtle Crossing Game using the turtle graphics library.
Classes Imported:
    - CrossingTurtle: Represents the player's turtle character.
    - Randomcars: Manages the creation and movement of random car obstacles.
    - Scoreboard: Handles score display and game over messages.
Global Variables:
    - screen (Screen): The main game window.
    - turtle (CrossingTurtle): The player's turtle character.
    - randomcar (Randomcars): The car manager for obstacles.
    - scoreboard (Scoreboard): The score and game over display.
    - pace (int): Controls the speed increment for cars as the game progresses.
    - points (int): Tracks the player's score.
    - proceed (bool): Controls the main game loop.
Game Controls:
    - Arrow keys (Up, Down, Left, Right): Move the player's turtle in respective directions.
Game Loop:
    - Updates the screen and moves cars at regular intervals.
    - Checks for collisions between the turtle and cars; ends the game if a collision occurs.
    - Checks if the turtle reaches the top of the screen; increases score, resets turtle position, and increases car speed.
    - Continues until a collision occurs.
Functions:
    - screen.onkeypress: Binds keyboard events to turtle movement methods.
    - randomcar.cars: Generates and moves car obstacles.
    - scoreboard.total_Score: Updates the score display.
    - scoreboard.game_over: Displays the game over message.
Exit:
    - screen.exitonclick: Waits for a mouse click before closing the game window.
Usage:
    Run this module to start the Turtle Crossing Game. Use the arrow keys to move the turtle and avoid cars to score points.
"""
from turtle import Screen  # Import the Screen class from the turtle module
from random import randint,choice  # Import randint and choice from random module
from crossing import CrossingTurtle,Randomcars,Scoreboard  # Import custom classes from crossing module
import time  # Import time module for sleep functionality

screen = Screen()  # Create a new screen object
screen.setup(height=600, width=600)  # Set up the screen size
screen.bgcolor("white")  # Set the background color to white
screen.title("TURTLE CROSSING GAME")  # Set the window title
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

turtle = CrossingTurtle()  # Create the player's turtle
randomcar = Randomcars()  # Create the random cars manager
scoreboard = Scoreboard()  # Create the scoreboard

# Set up keyboard controls for the turtle
screen.onkeypress(fun=turtle.fd, key="Up")  # Move forward on 'Up' key
screen.onkeypress(fun=turtle.down, key="Down")  # Move down on 'Down' key
screen.onkeypress(fun=turtle.left, key="Left")  # Move left on 'Left' key
screen.onkeypress(fun=turtle.right, key="Right")  # Move right on 'Right' key
screen.listen()  # Listen for keyboard events

pace = 0  # Initialize pace (speed increment for cars)
points = 0  # Initialize points (score)
proceed = True  # Game loop control variable

while proceed == True:  # Main game loop
    time.sleep(0.1)  # Pause for 0.1 seconds for smooth animation
    screen.update()  # Update the screen manually
    randomcar.cars()  # Generate and move cars

    for car in randomcar.car_list:  # Iterate through all cars
        if turtle.turtle.distance(car) < 25:  # Check collision with turtle
            proceed = False  # End game if collision detected
            scoreboard.game_over()  # Display game over message

        if turtle.turtle.ycor() >= 300:  # Check if turtle reached top
            points += 1  # Increment score
            turtle.turtle.goto(0, -280)  # Reset turtle position to start
            scoreboard.total_Score(score=points)  # Update scoreboard
            pace += 1  # Increase car speed for next round

        car.speed(10)  # Set car speed (animation speed)
        car.forward(5 + pace)  # Move car forward, increasing speed as pace increases

screen.exitonclick()  # Wait for user to click before closing the window