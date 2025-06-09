#here we are to goint o use conditionals to build a game
"""
A simple text-based adventure game called "Treasure Island".
The player is presented with a series of choices:
1. Choose a direction at a crossroad ("left" or "right").
2. If "left" is chosen, decide whether to "wait" for a boat or "swim" across a lake.
3. If "wait" is chosen, select one of three doors ("red", "yellow", or "blue") on an island.
Game outcomes:
- Choosing the wrong direction or action results in a "Game Over" message.
- Choosing the correct sequence leads to finding the treasure and winning the game.
Functions:
- tresure(): Handles the main game logic and user input for each decision point.
Note:
- All user input is case-insensitive.
- The game uses print statements for narration and input() for user interaction.
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to treasure island \n Your mission is to find the treasure')
def tresure():
    direction = input('You are at a cross roaad where do you want to go "left" or "right" \n')
    if direction.lower() == 'left':
        print('you\'ve come to the lake there is an island in the middle of the lake \n')
        dissicion = input('Type wait to wait for a boat or type swim to swim accros\n')
        if dissicion.lower() == 'wait':
            print('you arrived at the island unharmed. There is a hous with 3 doors \n')
            doors = input('Which door do you choose the red , yellow or blue door\n')
            if doors.lower() == 'red':
                print('!!! its a room full of fire Game Over !!!')
            elif doors.lower() == 'yellow':
                print('******You found the treasure you WIN******')
            elif doors.lower() == 'blue':
                print('!!! The room is full of sharks you loose !!!')
            else:
                print('enter door name properly')
        else :
            print(' !!! you get attack by sharks GAME OVER !!!')
    else:
        print(' !!! you fell into the weel GAME OVER !!!')
tresure()