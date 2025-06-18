

"""This script implements a simple Caesar cipher encryption and decryption tool that works with all ASCII letters, digits, spaces, and punctuation.
Modules:
    - string: Used to obtain a list of all ASCII letters, digits, and punctuation.
Global Variables:
    - letters_list: List containing all uppercase and lowercase ASCII letters, digits, space, and punctuation characters.
    - letter_list_size: The size of the letters_list.
Functions:
    encrypt():
        Prompts the user to enter a word and an encryption key.
        Encrypts the input word using the Caesar cipher algorithm by shifting each character by the key within the letters_list.
        Returns the encrypted word as a formatted string.
    decrypt():
        Prompts the user to enter an encrypted word and a decryption key.
        Decrypts the input word by reversing the Caesar cipher shift using the key within the letters_list.
        Returns the decrypted word as a formatted string.
Main Loop:
    - Continuously prompts the user to choose between encryption and decryption.
    - After each operation, asks the user if they want to continue or exit.
    - Handles invalid inputs gracefully and provides user-friendly prompts and messages.
Usage:
    Run the script and follow the on-screen prompts to encrypt or decrypt messages using a Caesar cipher with a customizable key."""

#today we are going to design a ciphering algorithim based on ceaser cipher
import string    #importing string module to obtain a list of characters
letters_list = list(string.ascii_letters + string.digits + ' ' + string.punctuation)  # letter_list a list containing uppercase,lowercase,space and gigits
letter_list_size = len(letters_list)  #lenght of letters_list size

def encrypt():   #encrypt function()

    user_input = list(input('Enter word to ecrypt : \n'))  #user input to collect encryption key and word to be encoded
    encryption_key = int(input('Enter encrypt key number : \n'))
    encrypted_word = ''   #empty string to contain the encoded word
    letter_list_size = len(letters_list)   
    
    for letter in user_input:  #for loop to iterate trhough each charater in user input
        letter_index = letters_list.index(letter)    # varaible to contain index of the iterated character
        
        encryt_letter_index = ((encryption_key + letter_index) % letter_list_size ) # Getting the index of the encrpted letter using modulus
        """
        this condition was set to avoid the 'index out of range error' because lets say example = [a,b] in a list and we want to push a by one 
        that will give us b , but if we want to push a by 3 it will give an out of range error so we will use modulus since if we want to count from a to b in a loop it will give us b 
        so we say 3 % the lenght of example which is 3%2 which = 1 , meaning item at index 1
         """
        encrypted_word += letters_list[encryt_letter_index] # adding it to encrpted_word string and continuing the iteration

    return f'encrypted word is $$$$$$$$$$$$$$   {encrypted_word}   $$$$$$$$$$$$'  #return the encrypted word

def decrypt():   #decrypt function

    user_input = list(input('Enter word to decrypt : \n')) #user input to collect decryption key and word to be decoded
    decryption_key = int(input('Enter Decrypt key number : \n'))
    decrypted_word = '' #empty string to contain the decoded word
    letter_list_size = len(letters_list)

    for letter in user_input: #for loop to iterate trhough each charater in user input
        letter_index = letters_list.index(letter)   # varaible to contain index of the iterated character

        decrypt_letter_index = ((letter_index - (decryption_key % letter_list_size)))  #similar to encrpytion this codition was set to avoid index out of range error 
        #simple math formular was use to get decrpty_letter_index   x + y = z meaning x = z - y
        decrypted_word+=letters_list[decrypt_letter_index]
        
    return f'decrypted word is $$$$$$$$    {decrypted_word}   $$$$$$$$$$$$'  #returnS the decrypted word-

option = True  #option set to true initialising the while loop

while option == True: # option called as condition in the while loop
    print('Welcome to Ceaphering algorithim')
    print("""
                     _                              _           
                      | |                            | |          
  ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 / __| '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
| (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
 \___|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
            __/ | |              __/ |         | |           __/ |
           |___/|_|             |___/          |_|          |___/ 
""")
    user_input = input('would you like to encrypt or decrypt enter \n type \'encode\' or \'decode\': \n' ) #user input to decide wether to encode or decode
    if user_input == 'encode':    #choices set for encoding or decoding
        print(encrypt())
    elif user_input == 'decode':
        print(decrypt())
    else:
        print('write encryption method properly')   
    

    decission = True  # desiccion set to treu to intialise the while loop
    while decission == True:   #decission called as condition in the while loop
        proceed = input('would you like to continue \'yes\' or \'no\' : \n')
        if proceed == 'no':   #the whole loop was writing so as to respect the coditions yes or no which are set else if user entry is not yes or no the while loop continues
            decission = False
            option = False
            print('thanks for using my program bye bye')    #if no the program stops

        elif proceed == 'yes':
            decission = False
            print('Okay lets continue')   # if yes program continues
        else:
            print('enter deccision correctly')  #enter decission correctly

        




