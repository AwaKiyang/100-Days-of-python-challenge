'''day 19 bro  '''
"""
This script creates an interactive drawing application using the turtle graphics library.
A turtle is displayed on the screen and can be controlled using keyboard inputs:
- Right Arrow: Move the turtle forward by 10 units.
- Left Arrow: Move the turtle backward by 10 units.
- 'w': Turn the turtle anticlockwise (left) by 10 degrees.
- 's': Turn the turtle clockwise (right) by 10 degrees.
- 'c': Reset the turtle's position to the center, clear the drawing, and lift/put down the pen.
The turtle is initialized with a green color and a moderate speed. The application listens for
keyboard events and exits when the screen is clicked.
"""
from turtle import Turtle, Screen
# Day 19 bro  
timmy_turtle = Turtle()
screen = Screen()

timmy_turtle.shape("turtle")     # Assign the turtle's shape
timmy_turtle.color('green')      # Set its color
timmy_turtle.speed(2)            # Set its speed

def move_forward():              # Function to move the turtle forward
    timmy_turtle.fd(10)         
def move_backwards():            # Function to move the turtle backward
    timmy_turtle.backward(10)
def anticlockwise():             # Function to turn the turtle anticlockwise
    timmy_turtle.left(10)
def clockwise():                 # Function to turn the turtle clockwise
    timmy_turtle.right(10)
def reset():                     # Function to reset the turtle's progress
    timmy_turtle.clear()         # Clear all progress on the screen
    timmy_turtle.penup()         # Lift the turtle's pen up
    timmy_turtle.home()          # Return the turtle to the original position
    timmy_turtle.pendown()       # Put the turtle's pen down

# onkeypress() method assigns functions to keyboard inputs for the turtle
screen.onkeypress(fun=move_forward, key="Right")   
screen.onkeypress(fun=move_backwards, key="Left")
screen.onkeypress(fun=anticlockwise, key="w")
screen.onkeypress(fun=clockwise, key="s")
screen.onkeypress(fun=reset, key="c")
screen.listen()                  # Make the screen listen for keyboard input
screen.exitonclick()
