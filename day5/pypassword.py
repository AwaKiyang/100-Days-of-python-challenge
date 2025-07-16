from random import *
"""
This script generates a random password based on user-specified criteria.

Features:
- Greets the user and displays ASCII art.
- Prompts the user to input the desired number of letters, numbers, and special characters for the password.
- Uses the `string` module to obtain lists of ASCII letters, digits, and punctuation characters.
- Randomly selects the specified number of characters from each category using the `choices` function from the `random` module.
- Shuffles the selected characters to ensure randomness.
- Concatenates the characters into a single password string and displays it to the user.

Functions:
- password():
    Prompts the user for password composition, generates and shuffles the password, and returns the final password string.

Dependencies:
- random
- string
"""
import string
print('\nWelcome to Pypassword generator\n ')
print('''
      ___________________
     /         \         \\
    /           \_________\\
   | =    =   =  | =  =  = |
   |             |         |
   | =    =   =  | =  =  = |
   |             |         |
   | =    =   =  | =  =  = |
   |             |         |
   | =    =   =  | =  =  = |
   |      ||     |         |
""""""""""""""""""""""""""""""""kOs
''')
letters = string.ascii_letters
numbers = string.digits
charact = string.punctuation #we used string functoin to create a list of letter,number and chracters
def password():
    letchoice = int(input('How many letters would you like to be in your password\n'))
    numchoice = int(input('How many numbers would you like to be in your password\n'))
    punctchoice = int(input('How many characters wolud you like to be in you password\n'))
    deal = choices(letters,k=letchoice) + choices(numbers,k=numchoice) + choices(charact,k=punctchoice) #we used choices function from random module to iterate from the respective live based on k number of times provided by the user\
    print(deal)
    shuffle(deal) # shuffling the deal list using shuffle function from random
    dams = ''
    for i in deal:
        dams+=i  #iterate from the shuffle deal to add its items to a string
        
    return f'your password is : {dams}'
    
print(password())
