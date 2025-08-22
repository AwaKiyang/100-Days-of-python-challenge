
# Import Turtle and Screen classes from turtle module, and randint from random module
"""
This script simulates a turtle race using the turtle graphics library.
Features:
- Initializes a graphical window for the race.
- Prompts the user to bet on which colored turtle will win.
- Creates six turtles, each with a unique color, and positions them at the starting line.
- Moves each turtle forward by a random distance in each iteration, simulating a race.
- Detects when a turtle crosses the finish line and announces the winner.
- Informs the user if their bet was correct or not.
- Keeps the window open until the user clicks to exit.
Modules Used:
- turtle: For graphical representation and turtle movement.
- random: For generating random movement distances.
Variables:
- screen: The main window for the race.
- user_bet: The color chosen by the user as their bet.
- colors: List of possible turtle colors.
- all_turtles: List holding all turtle objects.
- proceed: Boolean flag to control the race loop.
Usage:
Run the script and enter a color when prompted. Watch the turtles race and see if your chosen color wins.
"""
from turtle import Turtle, Screen
from random import randint
# Create a screen object
screen = Screen()
# Set up the screen size
screen.setup(width=500, height=400)
# Ask the user to bet on a turtle color
user_bet = screen.textinput(title='make you bet', prompt='Which turtle will win the race? Enter a color: ')

# List of turtle colors
colors = ['yellow', 'orange', 'blue', 'pink', 'green', 'red']
# Initial vertical spacing for turtles
spacing = 0
# List to hold all turtle objects
all_turtles = list()
# Create 6 turtles with different colors
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle
    new_turtle.color(colors[turtle_index])  # Set turtle color
    new_turtle.penup()  # Lift the pen to avoid drawing lines
    new_turtle.goto(x=-230, y=-100 + spacing)  # Position the turtle at the starting line
    spacing += 50  # Increase spacing for the next turtle
    all_turtles.append(new_turtle)  # Add turtle to the list

# Flag to control the race loop
proceed = True
# Start the race
while proceed == True:
    for turtle in all_turtles:
        # Check if the turtle has crossed the finish line
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print('you\'ve won')  # User wins
                proceed = False  # End the race
            else:
                print('youve lost')  # User loses
                proceed = False  # End the race
        # Move the turtle forward by a random amount
        turtle.forward(randint(0, 10))

# Keep the window open until the user clicks anywhere
screen.exitonclick()