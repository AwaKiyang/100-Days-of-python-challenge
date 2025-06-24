# Number Guessing Game

"""
This script implements an interactive number guessing game.

Overview:
---------
- The program generates a random number between 0 and 100 (inclusive).
- The user is prompted to choose a difficulty level: "easy" (10 attempts) or "hard" (5 attempts).
- The user then tries to guess the generated number within the allowed number of attempts.
- After each guess, the program provides feedback: "go higher" if the guess is too low, or "go lower" if the guess is too high.
- The game ends when the user either guesses the correct number or runs out of attempts.

Functions:
----------
difficultyt():
    - Prompts the user to select a difficulty level ("easy" or "hard").
    - Returns the number of attempts allowed based on the selected difficulty.
    - Handles invalid input by repeatedly prompting until a valid choice is made.

guessing(generated_number, attemps):
    - Runs the main guessing loop.
    - Prompts the user to enter guesses, provides feedback, and tracks remaining attempts.
    - Returns a success message if the user guesses correctly, or a failure message if attempts run out.

Usage:
------
1. Run the script.
2. The program will display a welcome message and prompt for a difficulty level.
3. Enter "easy" or "hard" to select the number of attempts.
4. Enter your guesses when prompted.
5. The program will guide you with feedback after each guess.
6. The game ends with a win or loss message.

Note:
-----
- Input validation is minimal; entering non-integer values for guesses will cause an error.
- The random number is printed at the start for debugging purposes; remove or comment out the print statement for a real game experience.
"""
print("""
$$$$$$\  $$\   $$\ $$$$$$$$\  $$$$$$\   $$$$$$\        $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$\      $$\  $$$$$$\  $$$$$$$\  $$$$$$$\  
$$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $\  $$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  \__|$$ |  $$ |$$ |      $$ /  \__|$$ /  \__|      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|$$ |$$$\ $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |
$$ |$$$$\ $$ |  $$ |$$$$$\    \$$$$$$\  \$$$$$$\        $$$$$$$  |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ $$ $$\$$ |$$ |  $$ |$$$$$$$  |$$ |  $$ |
$$ |\_$$ |$$ |  $$ |$$  __|    \____$$\  \____$$\       $$  ____/ $$  __$$ | \____$$\  \____$$\ $$$$  _$$$$ |$$ |  $$ |$$  __$$< $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |      $$\   $$ |$$\   $$ |      $$ |      $$ |  $$ |$$\   $$ |$$\   $$ |$$$  / \$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$  |\$$$$$$  |$$$$$$$$\ \$$$$$$  |\$$$$$$  |      $$ |      $$ |  $$ |\$$$$$$  |\$$$$$$  |$$  /   \$$ | $$$$$$  |$$ |  $$ |$$$$$$$  |
 \______/  \______/ \________| \______/  \______/       \__|      \__|  \__| \______/  \______/ \__/     \__| \______/ \__|  \__|\_______/ 
""")
from random import randint  #form random module i imported randint function
number = randint(0,101) #assigned a varaibel to store random generated number from 0 to 100
print(number)
print("welcome to the number guessing game i am thinking of a number between 0 and 100")

def difficultyt(): # function to get game difficulty hard or easy and generate number of attemps
    num_attempts = 0   # number of attempt set to zero by default

    level = True  #intailinzation of the while loop
    while level == True:  #beggining of while loop
        difficulty = input("Enter difficulty to proceed in the game \"HARD\" or \"EASY\" : \n").lower()  #prompt to get user dificulty
        if difficulty == 'easy': #condition to work if difficult chosen is easy
            print("******you chosed easy mode you have 10 guessing attemps : *****")
            num_attempts = 10 #num_attempts now becomes ten giving 10 life to the user
            level = False  #level set to false to end the while loop
        elif difficulty == 'hard':  #condition to work if difficult chosen is hard
            print("*******you chosed easy mode you have 5 attempts : ********")
            num_attempts = 5  #num_attempts now becomes five giving 5 life to the user
            level = False #level set to false to end the loop
        else:
            print("!!!!!!enter difficulty properly!!!!!!")  #fault tolerance incase difficulty is no perperly set the while loop continues until difficulty is properly spell

    return num_attempts  #giving the function the value num_attempts

lives = difficultyt()  # assiging difficulty value to lives

def guessing(generated_number,attemps): #funtion guessing() with parameters set to collect generated number and attempt
    
    life = 0 #initialization of the while loop life set to zero
    while life < attemps:  #condition set to function while life is less than attempts
        user_guess = int(input("enter number to guess : "))  #collecting user guesses to work with them
        if user_guess < generated_number: #conditionset to print go hisher is user guess is lower than generated number
            print("go higher !!")
        if user_guess > generated_number: #conditionset to print go lower is user guess is higher than generated number
            print("go lower !!")

        if generated_number == user_guess:  #if user guess is equivalent to generated number
            return f"$$$$$$perfect you have found it {user_guess} was the correct guess $$$$$"  # return message displayed incase of success
        elif life == (attemps - 1): #condition set to display failure message if user attempts is zero
            return f'sorry you are left with 0 attempts you\'ve lost'
        else: #condition set to increase life by one incase user is incorrect , by increase life_used user attempts decrease 
            life+=1
            print(f'continue its not correct you are left with {attemps-life} attemptss')

print(guessing(generated_number = number, attemps = lives)) #calling the function to start program