
"""
# Snake Game Main Script
This script initializes and runs the main loop for a classic Snake game using the turtle graphics library.
It manages the game window, snake movement, food consumption, scoring, and collision detection.
Imports:
    - Imports Turtle graphics classes for drawing and handling the game window.
    - Imports custom Snake and Scoreboard classes for game logic and score display.
    - Imports time module for controlling game speed.
Screen Setup:
    - Creates the main game window.
    screen.setup(width=600, height=600)
    - Sets the window size to 600x600 pixels.
    - Sets the background color to black.
    - Sets the window title.
    - Turns off automatic screen updates for smoother animation.
Game Object Initialization:
    - Creates a Snake object to manage the snake's segments and movement.
    - Creates a Scoreboard object to display and update the score.
Snake and Food Setup:
    - Initializes the snake's starting segments.
    - Places the first food item on the screen.
Game Loop Control:
    - Boolean flag to control the main game loop.
    - Initializes the player's score.
Main Game Loop:
        - Manually updates the screen for smooth animation.
        - Pauses briefly to control the snake's speed.
        - Moves the snake forward in its current direction.
        - Handles user input for snake direction.
    # Food Collision Detection
        - Places new food when the snake eats the current food.
        score += 1
        - Increments the score.
        - Updates the displayed score.
        - Adds a new segment to the snake's body.
    # Wall Collision Detection
        - Displays a message for wall collision.
        - Ends the game loop.
    # Self Collision Detection
            - Displays a message for self collision.
            - Ends the game loop.
Game Exit:
    - Waits for a mouse click to close the game window.
"""
from turtle import Turtle,Screen  # Import Turtle graphics classes
from snake_game import Snake, Scoreboard  # Import custom Snake and Scoreboard classes
import time  # Import time module for controlling game speed
from turtle import Turtle, Screen  # Redundant import, but imports Turtle and Screen again

screen = Screen()  # Create the main game window
screen.setup(width=600,height=600)  # Set window size to 600x600 pixels
screen.bgcolor('black')  # Set background color to black
screen.title("My snake game")  # Set window title
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

snake = Snake()  # Create a Snake object
scoreboard = Scoreboard()  # Create a Scoreboard object

snake.create_snake()  # Initialize the snake's starting segments
snake.snake_food()  # Place the first food item on the screen
proceed = True  # Boolean flag to control the main game loop
score = 0  # Initialize the player's score

while proceed == True:  # Main game loop
    screen.update()  # Manually update the screen for smooth animation
    time.sleep(0.15)  # Pause briefly to control the snake's speed
    snake.move_snake()  # Move the snake forward in its current direction
    snake.control_snake()  # Handle user input for snake direction

    # Food Collision Detection
    if snake.snake_list[0].distance(snake.food) < 15:  # Check if snake head is close to food
        snake.snake_food()  # Place new food
        score+=1  # Increment the score
        scoreboard.total_score(score)  # Update the displayed score
        snake.add_segment()  # Add a new segment to the snake's body

    # Wall Collision Detection
    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].ycor() > 280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() < -280:
       scoreboard.wall_collisoin()  # Display a message for wall collision
       proceed = False  # End the game loop

    # Self Collision Detection
    for i in range(1, len(snake.snake_list)):  # Check collision with snake's own body
        if snake.snake_list[0].distance(snake.snake_list[i]) < 15:
            scoreboard.wall_collisoin()  # Display a message for self collision
            proceed = False  # End the game loop

screen.exitonclick()  # Wait for a mouse click to close the game window
