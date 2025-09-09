
"""
This script implements a U.S. States guessing game using the turtle graphics library and pandas for data handling.
Workflow:
- Loads state names and their coordinates from a CSV file.
- Displays a blank map of the U.S. as the game background.
- Prompts the user to guess state names.
- When a correct guess is made, the state name is displayed at its corresponding location on the map.
- The game continues until the user enters an incorrect state name, at which point the game ends.
Classes:
- State_location: Handles displaying state names and game over messages on the turtle screen.
Key Variables:
- df_states: DataFrame containing state names and coordinates.
- states_list: List of all state names.
- x_list, y_list: Lists of x and y coordinates for each state.
- states_and_coordinates: List of dictionaries, each containing a state and its coordinates.
Main Loop:
- Repeatedly prompts the user for a state name.
- If the guess is correct, displays the state name on the map.
- If the guess is incorrect, ends the game.
Usage:
- Requires "50_states.csv" with columns: state, x, y.
- Requires "blank_states_img.gif" as the map background.
- Requires a "states_turtle.py" module with State_location class.
"""
import pandas as pd     # Importing the pandas library
from turtle import Screen  # Importing the Screen class from the turtle module
from states_turtle import State_location  # Importing the State_location class from the states_turtle module
st = State_location()  # Creating an object st
screen = Screen()  # Initializing the screen
screen.title("US STATES GAME")  # Setting the screen title
screen.bgcolor("black")  # Setting the screen background color
screen.setup(height=510, width=740)  # Setting the screen dimensions
screen.bgpic("blank_states_img.gif")  # Setting the background image

df_states = pd.read_csv("50_states.csv")  # Creating the df_states DataFrame from "50_states.csv" using pandas
states_dict = df_states.to_dict()  # Converting the DataFrame into a dictionary

states_list = df_states["state"].to_list()  # Creating a list states_list from the "state" column in the df_states DataFrame
x_list = df_states["x"].to_list()  # Creating a list x_list from the "x" column
y_list = df_states["y"].to_list()  # Creating a y_list from the "y" column

states_and_coordinates = list()  # Creating a list to contain both states and coordinates

for i in range(len(states_list)):  # Looping through the length of states_list
    # Appending a dictionary of state, x, and y into states_and_coordinates to create a list of dictionaries representing distinct states and their respective coordinates
    states_and_coordinates.append({"state": states_list[i], 'x': x_list[i], 'y': y_list[i]})

correct_guesses = 0 #intialixing variable to increment by on number of correct guesses

proceed = True  # Setting proceed to True
while proceed:  # Initializing the game loop
    # Collecting user input from the screen to ask the user to guess a state found on the map and showing number or correcying guesses
    user_input = screen.textinput(title=f"{correct_guesses}/50 states correct", prompt="Which state do you know about: ").capitalize()
    if user_input in states_list:  # If user_input is in states_list
        # Looping through each state and coordinate from the states_and_coordinates list of dictionaries
        for states in states_and_coordinates:
            if user_input == states["state"]:  # If user_input matches a particular state in the dictionary
                # Calling the set_location() method from the st object to set the state name on the map based on its respective coordinates
                st.set_location(x_cor=states["x"], ycor=states["y"], state_name=states["state"])
                correct_guesses += 1 #Tracking the number of correct guesses.
    else:  # If the condition is not met
        st.game_over(score= correct_guesses)  # Calling the game_over() method to stop the game
        proceed = False  # Setting proceed to False, thus ending the while loop
screen.exitonclick()  # Setting the screen to exit on click
