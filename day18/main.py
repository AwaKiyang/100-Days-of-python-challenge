"""
This script demonstrates various exercises using the Python turtle graphics module.
It includes functions to draw geometric shapes, patterns, and perform random movements
with the turtle. The script is intended for learning and experimenting with turtle graphics.
Functions:
----------
triangle():
    Draws a triangle with specific colors and widths, moves the turtle, and clears the screen.
color_pattern():
    Draws a colorful spiral pattern by iterating through a set of colors and rotating the turtle.
star():
    Draws a star-like shape using the turtle, sets its shape and color, and displays its position.
test():
    Writes a string on the turtle screen with specified alignment and font.
draw_sqaure():
    Draws a green square using the turtle and waits for the user to close the window.
dashed_line():
    Draws a dashed line by alternating between pen up and pen down states.
crazy_shapes():
    Draws polygons from triangle to decagon, each with a different color.
random_mov():
    Moves the turtle in random directions and colors, creating a random walk pattern.
Global Variables:
-----------------
timmy_turtle:
    An instance of the Turtle class used for drawing shapes and patterns.
screen:
    An instance of the Screen class used to display the turtle graphics window.
Notes:
------
- Some functions are commented out and not executed by default.
- The script uses both procedural and object-oriented approaches with the turtle module.
- The random_mov() function runs an infinite loop and must be stopped manually.
Here am doing some exercises on how to use the turtle module 
"""
from turtle import *
def triangle():
    forward(100) #forward enables the turtle to move forward by 100 steps
    left(120) #left rotates the turtle by 120 degrees
    color('blue') #change the color of the turtle
    width(7) #change the width of the turtle
    up() #up function lift the pen up
    forward(120) 
    down() #while the down function brings back the pen down
    left(130)
    color('green')
    forward(120)
     # sends you turtle back to its starting point after its finished its previous processes
    #backward() moves the turtle by x steps behind
    #rigth() rotates by 
    clearscreen() #enables you to clear the screen

#triangle()

def color_pattern():
    for steps in range(100):
        for c in ('blue','red','green'):
            color(c)
            forward(steps)
            right(30)

#color_pattern()

def star():
    shape('turtle')
    width(10)
    color('blue')
    fillcolor('yellow')
    left(75)
    forward(100)
    left(30)
    forward(100)
    right(10)
    forward(100)
    position()#to know the exact coordinates of the turtle
    exitonclick()
star()


def test():
    write('Awa Precious Kiyang', True, align='center', font=('Arial', 8, 'normal'))
    exitonclick()
#test()


from turtle import Turtle, Screen  # from the turlte module we inport Turtle and Screen
timmy_turtle = Turtle() #assign turtle class to timmy_turle varable
screen = Screen() #assigning the screen class to the screen varaible

def draw_sqaure():
    '''function used to draw a circle using the turtke module'''
    timmy_turtle.color("green")       #changing the color of the turtlr
    for i in range(4):       #using for loop for repeating procees 4 times
        timmy_turtle.forward(100)       #telling the turtle to move by 100 steps by using the forward() method
        timmy_turtle.left(90)           #telling the turtle to turn left by 90deg using the left()
    screen.exitonclick()       #using the exitonclick method so as to close the window manually
#draw_sqaure()       #calling the function


def dashed_line():    #calling dash_line function
    '''drawing a dashed lines'''
    for i in range(30):   #iterating using the range function
        timmy_turtle.forward(12)
        timmy_turtle.penup()
        timmy_turtle.forward(12)
        timmy_turtle.pendown()
    screen.exitonclick()
#dashed_line()    #calling function


from random import choices
def crazy_shapes():
    '''Drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon and more'''
    color = ["blue","gray","yellow","orange","green","red","pink"]     #declaring color list which we will iterate through to have different colored shapes
    color_choice = 0 #color_choice which will be used as argument for iteration through the color list and has an incremental scope
    '''NB ###for angle in range(3,11):###is the most important part cause it determines the number of shapes to be created'and thier angles''' 
    for num_side in range(3,11):   #using for loop  range function to set the angle and number of sides our turtle will be switching to after every shape is completed  
        angle = num_side     #angle of side of our shape
        for side in range(num_side):    #for loop and range function for iteration using num_side varaible value
            timmy_turtle.right(360/angle)   #angle or our turtle for shape creation
            timmy_turtle.forward(100)     
        timmy_turtle.color(color[color_choice % len(color)])   #turtle color is set from iterating through the color list and combined with modulus operate for looping through the list
        color_choice+=1  #color chioce incremented for change in color
    screen.exitonclick()    
#crazy_shapes()  #calling the function

from random import choice
def random_mov():
    '''random turtle movement'''
    angles = [0,90,180,270]  #angles our turtle is going to use
    color = ["blue","gray","yellow","orange","green","red","pink"] #color of our turtle
    t = True
    while t == True:  #while loop for infite looping
        timmy_turtle.pensize(5)  #turtle method() for width of our tutle
        timmy_turtle.forward(40)
        timmy_turtle.setheading(choice(angles)) #setheading() method combined with reandom angle as argument for turtle direction
        timmy_turtle.color(choice(color)) 
    screen.exitonclick()
random_mov()
