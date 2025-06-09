from random import *
"""A simple Hangman game implementation in Python.
This script randomly selects a word from a predefined list and allows the user to guess letters.
The user has up to 6 incorrect guesses before losing the game. The game displays ASCII art
representing the hangman at each stage of incorrect guesses.
Modules:
    random: Used for randomly selecting a word from the list.
Variables:
    hang1, hang2, hang3, hang4, hang5 (str): ASCII art representing the hangman at different stages.
    list_word (list): List of possible words to guess.
    ran_word (str): Randomly selected word from list_word.
    Answer (list): The selected word converted to a list of characters.
    Answer_space (list): List representing the current state of guessed letters and underscores.
    hang_stage (list): List of hangman ASCII art stages.
Functions:
    HangMan():
        Runs the main game loop for Hangman.
        Prompts the user to guess letters, updates the game state, and displays the hangman stages.
        Returns a string indicating whether the user has won or lost the game.
Usage:
    Run the script to start a game of Hangman in the console.
"""
hang1 = """
   _______
     |/      
     |      (_)
     |      \|/
     |       
     |  
     |
 jgs_|___
"""
hang2 = """
   _______
     |/      
     |      (_)
     |      \|/
     |       |
     |    
     |
 jgs_|___
"""
hang3= """
   _______
     |/      
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___
"""
hang4 = """
   _______
     |/      
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 jgs_|___
"""
hang5 = """
   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 jgs_|___

"""

print("""
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"   
""")
#
list_word = ['muyer','emmanuel','plum'] # here is our list containing words
ran_word = choice(list_word) #random.choice() permits us to randomly select any word from the list
Answer = list(ran_word) #we convert the selected word into a list
Answer_space = list() #list containig spaces based on the number of items in our anwer list
for i in range(0,len(Answer)):
    Answer_space.append('_')  #appending '_' which represent our spaces in the Anwer_space list based on the number of items found in the Anawe list
print(Answer,Answer_space)
#
hang_stage = [hang1,hang2,hang3,hang4,hang4,hang5]   #list which will enable us iterate through the variuios images
#
def HangMan(): #defining our hangman function
    life = 0 # life set a 0 for incrementaion in the while loop
    die_bro = 0 # it will be use to iterate through the hangstage list
    while life<6:  # while loop which will stop when life varaible will be greater than 6

        user_input = input('enter word to check : ')  # user input
        letter_indexes = [let_index for let_index, letter in enumerate(Answer) if letter == user_input] # list comprehenhesion plus enumartion used to iterate through the answer list to find all items and thier indexes so as to know thier occurence

        if user_input in Answer and user_input not in Answer_space: #condition set to functoin if user_input is not found in anwser and anser_space
            for indexes in letter_indexes:     # iterating through the letter_indexes list so as to get the index(es) of the letter from user input found in answer list and be able to replace them with thier correspondiind idex of Answer_space list
                Answer_space[indexes] = user_input  #changing spaces with words from user input
            print(f'{user_input} is in {Answer_space} a index(es) {letter_indexes}') 
        elif user_input in Answer and user_input in Answer_space: #condition set to function if user input is found in answer and answer_space list
            life+=1  # if condition met life increases by one 
            print(hang_stage[die_bro]) #printing hang image by iterating through hang_stage list
            print(f'****************You\'ve already entered this letter {user_input} youre left with {6-life}/6********************')  #printing failure message
            die_bro+=1 # if condition met die_bro increases by one an proceeds to the next imag in hang_stage list incase of failure
        else:
            life+=1 # if non of the above conditions are met life increases to one
            print(hang_stage[die_bro])  #printing hang image by iterating through hang_stage list
            print(f'****************Letter {user_input} is not in the word Your are left with {6-life}/6********************') #printing failure message
            die_bro+=1 # if condition met die_bro increases by one an proceeds to the next imag in hang_stage list incase of failure

        if '_' not in Answer_space: # checking if user has found all letters in the word
            life += 6 # if conditions met life increase by 6 so as to stop the while loop 
            return f'$$$$$$$$$$$$$$$$$$$$You\'ve Won congrats$$$$$$$$$$$$$$$$$$$$$$' #printing success message user has won
        
    if life == 6: # checking if life has reached 6 remember life varaible was set at zero and increases each time user fails and while loop conditiion was set to (life<6)
        return '****************You\'ve lost****************'  ##final chance was given user lost the game
print(HangMan()) #calling hangman function