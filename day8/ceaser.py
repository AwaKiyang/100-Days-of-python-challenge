"""
ceaser.py

This module implements a simple Caesar cipher encryption and decryption algorithm.

Overview
--------
The Caesar cipher is a substitution cipher where each character in the plaintext
is shifted by a fixed number of positions down a defined character set. This
implementation supports uppercase and lowercase English letters, digits, and the
space character.

Functions
---------
encrypt():
    Prompts the user to enter a word and a key, then returns the encrypted word
    using a Caesar cipher shift based on the provided key. Handles key values
    larger than the character set size by using modulus arithmetic.
decrypt():
    Prompts the user to enter an encrypted word and a key, then returns the
    decrypted word by reversing the Caesar cipher shift using the provided key.
    Handles key values larger than the character set size by using modulus arithmetic.

Main Loop
---------
The script runs an interactive loop that allows the user to choose between
encryption and decryption, and to continue or exit after each operation.

Variables
---------
letters_list : list
    List of all characters supported by the cipher (uppercase, lowercase, digits, space).
letter_list_size : int
    The size of the letters_list.

Usage
-----
Run the script and follow the prompts to encrypt or decrypt messages using a Caesar cipher.

Example
-------
$ python ceaser.py
Welcome to Ceaphering algorithim
would you like to encrypt or decrypt enter 
 type 'encode' or 'decode': 
encode
Enter word to ecrypt : 
Hello123
Enter key number : 
5
encrypted word is $$$$$$$$$$$$$$   Mjqqt678   $$$$$$$$$$$$

Notes
-----
- The cipher only works with characters present in the defined letters_list.
- If a character not in the list is entered, a ValueError will be raised.
- The script uses modulus arithmetic to handle key values larger than the character set size.
"""
#today we are going to design a ciphering algorithim based on ceaser cipher
import string    #importing string module to obtain a list of characters
letters_list = list(string.ascii_letters + string.digits + ' ')  # letter_list a list containing uppercase,lowercase,space and gigits
letter_list_size = len(letters_list)  #lenght of letters_list size

def encrypt():   #encrypt function

    user_input = list(input('Enter word to ecrypt : \n'))  #user input to collect encryption key and word to be encoded
    encryption_key = int(input('Enter key number : \n'))
    encrypted_word = ''   #empty string to contain the encoded word
    letter_list_size = len(letters_list)   
    
    for letter in user_input:  #for loop to iterate trhough each charater in user input
        letter_index = letters_list.index(letter)    # varaible to contain index of the iterated character
        
        if encryption_key >= letter_list_size:  #condition defined to function if encryption key is >= letter_list_size
            moduling = encryption_key % letter_list_size 
            """
            this condition was set to avoid the 'index out of range error' because lets say example = [a,b] in a list and we want to push a by one 
            that will give us b , but if we want to push a by 3 it will give an out of range error so we will use modulus since if we want to count from a to b in a loop it will give us b 
            so we say 3 % the lenght of example which is 3%2 which = 1 , meaning counting a to b  by 3 is similar to puahing a by 1 since encrpytion key 3 is larger than the lenght of example
            """
            encryt_letter_index = ((letter_index + moduling) - letter_list_size) # Getting the index of the encrpted letter
            encrypted_word += letters_list[encryt_letter_index] # adding it to encrpted_word string and continuing the iteration
        else:
            encryt_letter_index = ((letter_index + encryption_key) - letter_list_size)  # if encrption_key does not surpass the list len the we proceed 
            encrypted_word += letters_list[encryt_letter_index]

    return f'encrypted word is $$$$$$$$$$$$$$   {encrypted_word}   $$$$$$$$$$$$'  #return the encrypted word

def decrypt():   #decrypt function

    user_input = list(input('Enter word to decrypt : \n')) #user input to collect decryption key and word to be decoded
    decryption_key = int(input('Enter Decrypt key number : \n'))
    decrypted_word = '' #empty string to contain the decoded word
    letter_list_size = len(letters_list)

    for letter in user_input: #for loop to iterate trhough each charater in user input
        letter_index = letters_list.index(letter)   # varaible to contain index of the iterated character

        if decryption_key >= letter_list_size:  #condition defined to function if decryption key is >= letter_list_size
            moduling = decryption_key % letter_list_size  #similar to encrpytion this codition was set to avoid index out of range erro
            decrypt_letter_index = ((letter_index - moduling))
            decrypted_word+=letters_list[decrypt_letter_index]
        
        else:  #if decrption_key does not surpass the list len the we proceed 
            decrypt_letter_index = ((letter_index - decryption_key))
            decrypted_word+=letters_list[decrypt_letter_index]
    return f'decrypted word is $$$$$$$$    {decrypted_word}   $$$$$$$$$$$$'  #returnS the decrypted word

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

        




