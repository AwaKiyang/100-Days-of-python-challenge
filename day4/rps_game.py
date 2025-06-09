from random import randint
"""A simple Rock, Paper, Scissors game implementation.
This script allows a user to play Rock, Paper, Scissors against the computer.
The user is prompted to enter a choice (0 for Rock, 1 for Paper, 2 for Scissors).
The computer randomly selects its choice, and the result is displayed with ASCII art.
Functions:
    rps_game(n): Takes the user's choice as an integer (0, 1, or 2), compares it with the computer's random choice,
                 prints the corresponding ASCII art and the game result (win, lose, or draw), and returns a thank you message.
Variables:
    rock (str): ASCII art representing rock.
    paper (str): ASCII art representing paper.
    scisors (str): ASCII art representing scissors.
    game_choice (list): List containing the ASCII art for rock, paper, and scissors.
Usage:
    The script prompts the user for input and displays the result of the game.
"""
rock = """
                        _    
                | |   
    _ __ ___   ___| | __
    | '__/ _ \ / __| |/ /
    | | | (_) | (__|   < 
    |_|  \___/ \___|_|\_
"""
paper = """              
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
"""
scisors = """                      
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ 
|___/\___|_|___/___/\___/|_|  |___/
                                   
"""


game_choice = [rock,paper,scisors]
def rps_game(n):
    computer_choice = randint(0,2)
    if n == computer_choice :
        print(f'{game_choice[n]}\nComputer chose\n{game_choice[computer_choice]}\n DRAW')
    elif n ==0 and computer_choice == 1:
        print(f'{rock}\nCOmputer Chose\n{paper}\nYou Lose')
    elif n == 0 and computer_choice == 2:
        print(f'{rock}\nComputer Chose\n{scisors}\n****YOU WIN****')
    elif n == 1 and computer_choice == 0:
        print(f'{paper}\nComputer Chose\n{rock}\n****YOU WIN****')
    elif n == 1 and computer_choice == 2:
        print(f'{paper}\nComputer Chose\n{scisors}\nYou Lose')
    elif n == 2 and computer_choice == 0:
        print(f'{scisors}\nComputer Chose\n{rock}\nYou Lose')
    elif n == 2 and computer_choice == 1:
        print(f'{scisors}\nComputer Chose\n{paper}\n***YOU WIN***')
    else:
        print('Enter number corretly')
    return 'thanks for playing'
n = int(input('!!!!Welcome to rock, paper, scissors\nWhat do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n '))
print(rps_game(n))