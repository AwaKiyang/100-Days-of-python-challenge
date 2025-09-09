'''This script converts a user's name into its NATO phonetic alphabet equivalent.
Functionality:
- Prompts the user to enter their name.
- Converts the input to uppercase to match the format of the NATO phonetic alphabet.
- Reads a CSV file ("nato_phonetic_alphabet.csv") containing the NATO phonetic alphabet into a pandas DataFrame.
- Creates a dictionary mapping each letter to its corresponding phonetic code.
- Generates a list of phonetic codes for each letter in the user's input using dictionary comprehension.
- Alternatively, demonstrates how to achieve the same result by filtering the DataFrame for each letter.
- Prints the resulting list of phonetic codes.
Notes:
- The script includes commented examples of looping through DataFrame rows using `iterrows()`.
- Assumes the CSV file has columns "letter" and "code".'''

import pandas as pd  # Import the pandas library for data manipulation
user_input = input("enter your name : ").upper()  # Get user input and convert to uppercase
df_nato = pd.read_csv("nato_phonetic_alphabet.csv")  # Read the NATO phonetic alphabet CSV into a DataFrame

phonetic_dict = {row.letter : row.code for (index,row) in df_nato.iterrows()}   # Create a dictionary mapping each letter to its phonetic code
output_list = [phonetic_dict[letter] for letter in user_input]  # Generate a list of phonetic codes for each letter in the user input
print(output_list)  # Print the resulting list

"""
OR
"""

name_letter = [letter for letter in user_input]  # Create a list of letters from the user input
waar = []  # Initialize an empty list to store phonetic codes
for let in name_letter:  # Loop through each letter in the input
    name = df_nato[df_nato["letter"] == let]  # Filter the DataFrame for the current letter
    waar.append(name.code.item())  # Append the corresponding code to the list

print(waar)  # Print the resulting list

'''# Looping through rows of a dataframe using iterrows()
for (index,row) in df_nato.iterrows():
    print(index) # Print the index of the current row
    print(row.code) # Print the value in the 'code' column for the current row
    print(row.letter) # Print the value in the 'letter' column for the current row'''
