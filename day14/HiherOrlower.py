#today we are goint o be bulding a higher or lower game
'''This script implements a simple "Higher or Lower" quiz game in Python.
Features:
- Displays ASCII art banners at the start of each question.
- Presents a series of questions where the user must choose between two options (A or B) based on which has a higher value (e.g., more followers, more users).
- Tracks and displays the user's score after each question.
- Ends the game immediately upon the first incorrect answer, displaying the final score.
Global Variables:
- text1 (str): ASCII art banner displayed at the start of each question.
- text2 (str): ASCII art separator between options.
- questionss_list (list): List of dictionaries, each containing:
    - 'optionA' (str): Description of the first option.
    - 'optionB' (str): Description of the second option.
    - 'Answer' (str): The correct answer ('A' or 'B').
    - 'Question' (str): The question prompt for the user.
Functions:
- quiz(questionss_list):
    Iterates through the list of questions, prompting the user for input and updating the score.
    Ends the game and returns the final score if the user answers incorrectly.
Usage:
- Run the script to start the quiz. The user will be prompted to answer each question by typing 'A' or 'B'.'''


text1 = """
 | |  | |_   _/ ____| |  | |
 | |__| | | || |  __| |__| |
 |  __  | | || | |_ |  __  |
 | |  | |_| || |__| | |  | |
 |_|  |_|_____\_____|_|  |_|
 | |    / __ \ \        / / 
 | |   | |  | \ \  /\  / /  
 | |   | |  | |\ \/  \/ /   
 | |___| |__| | \  /\  /    
 |______\____/   \/  \/    
                           
"""
text2 = """

\ \ / / __|
 \ V /\__ \\
  \_/ |___/
           """
questionss_list = [
    {'optionA' : 'Zendaye is an American actress and musician from the united states','optionB' : 'Christiano ronaldo a pottuguese player', 'Answer' : 'A', 'Question' : 'who has more followers?'},
    {'optionA': 'Instagram, a popular photo sharing app', 'optionB': 'Twitter, a microblogging platform', 'Answer': 'A', 'Question': 'Which platform has more active users? '},
    {'optionA': 'Lionel Messi, an Argentine footballer', 'optionB': 'Neymar Jr, a Brazilian footballer', 'Answer': 'A', 'Question': 'Who has more Instagram followers? '},
    {'optionA': 'YouTube, a video sharing platform', 'optionB': 'Facebook, a social networking site', 'Answer': 'B', 'Question': 'Which platform has more monthly active users? '},
    {'optionA': 'Ariana Grande, an American singer', 'optionB': 'Selena Gomez, an American singer and actress', 'Answer': 'B', 'Question': 'Who has more Instagram followers? '},
    {'optionA': 'Dwayne "The Rock" Johnson, an actor and wrestler', 'optionB': 'Kylie Jenner, a media personality', 'Answer': 'B', 'Question': 'Who has more Instagram followers? '},
    {'optionA': 'TikTok, a short-form video platform', 'optionB': 'Snapchat, a multimedia messaging app', 'Answer': 'A', 'Question': 'Which platform has more global downloads? '},
    {'optionA': 'Bill Gates, co-founder of Microsoft', 'optionB': 'Elon Musk, CEO of Tesla and SpaceX', 'Answer': 'B', 'Question': 'Who has more Twitter followers? '},
    {'optionA': 'Taylor Swift, an American singer-songwriter', 'optionB': 'Katy Perry, an American singer', 'Answer': 'A', 'Question': 'Who has more Instagram followers? '},
    {'optionA': 'Google, a search engine', 'optionB': 'Bing, a search engine', 'Answer': 'A', 'Question': 'Which search engine has more users? '},
    {'optionA': 'Barack Obama, former US President', 'optionB': 'Donald Trump, former US President', 'Answer': 'A', 'Question': 'Who has more Twitter followers? '}
]   #here we have created a list of dictionaries containing diferent questions, Answers and options which will be iterated trough

def quiz(questionss_list): #created my quiz function wich takes questions_list a parameter
    score = 0  #intialized my score to zero so as to increase if user provides correct answers
    for question in questionss_list:  #iterating through the list
        print(text1)  #printing ascii character
        print('your current score is : ',score)  #printing user score a user proceed through the game
        print(f'Compare A : {question['optionA']} ')  #first option optained from the iterated item in the list of dictionaries with key [optionA]
        print(text2)  #print ascii charater
        print(f'Compare B : {question['optionB']}') #second option obtained from the iterated item in the list of dictionaries with key  [optionB]
        user_input = input(f'{question['Question']} \'A\' or \'B\' : ').upper()  # getting user input A or B based on question provided by iterated item with the key [Questions]
        if user_input == question['Answer']: #condition set to proceed if user input in equivalent to value of tierated item in the list of dictionaries having key [Answers]
            score+=1 #if condition is met score increses by one
        else:
            return f'youve lost your final score is {score}' #else if user anwer if incorect the program ends giving user final score
        
print(quiz(questionss_list)) #printing the quiz() function