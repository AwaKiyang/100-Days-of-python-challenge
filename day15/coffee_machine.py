#creating a coffee machine
'''Main Features:
--------------
- Handles coin input (quarters, dimes, nickels, pennies) and calculates change.
Data Structures:
----------------
- `cappucino`, `expresso`, `latte`: Dictionaries defining the resource requirements and price for each drink.
- `water_quantity`, `milk_quantity`, `coffee_quantity`, `amount_sold`: Global variables tracking the machine's resources and sales.
----------
- `purchase(drink)`: 
    Processes the purchase of a selected drink. Checks if there are enough resources to make the drink, prompts the user for coin input, calculates if the payment is sufficient, returns change if necessary, updates the resources, and returns a message indicating the result of the transaction.
    Parameters:
        - drink (dict): A dictionary containing the drink's name, required water, coffee, milk, and price.
    Returns:
        - str: A message indicating the result of the purchase (success, insufficient resources, or insufficient payment).
- `report()`:
    Prints the current status of water, milk, coffee, and total amount sold.
- `system()`:
    Main loop that interacts with the user, processes commands, and manages the coffee machine's operation. Accepts user input to select drinks, print reports, or turn off the machine. Handles invalid input gracefully.
------
Coin Values:
------------
- Penny:   $0.01
- Nickel:  $0.05
- Dime:    $0.10
- Quarter: $0.25
Drink Recipes:
--------------
- Espresso:  50ml water, 18g coffee, 0ml milk,   $1.50
- Latte:    200ml water, 24g coffee, 150ml milk, $2.50
- Cappuccino:250ml water, 24g coffee, 100ml milk, $3.00
Example Interaction:
--------------------
- User selects a drink.
- Machine checks resources and prompts for coins.
- If payment is sufficient, drink is served and change is returned.
- User can request a report or turn off the machine at any time.
Note:
-----
All resource and sales tracking is done using global variables. The script is intended for interactive use in a terminal or command prompt.
Coffee Machine Simulation
This script simulates a coffee machine that can serve three types of coffee drinks: espresso, latte, and cappuccino.
It manages resources (water, milk, coffee), processes user payments, and tracks the total amount sold.
Features:
- Allows users to purchase drinks if sufficient resources are available.
- Handles coin input and calculates change.
- Provides a report of remaining resources and total sales.
- Supports turning off the machine and handling invalid input.
Functions:
- purchase(drink): Processes the purchase of a selected drink, checks resources, handles payment, and updates resources.
- report(): Prints the current status of water, milk, coffee, and total amount sold.
- system(): Main loop that interacts with the user, processes commands, and manages the coffee machine's operation.
Data:
- cappucino, expresso, latte: Dictionaries defining the resource requirements and price for each drink.
- water_quantity, milk_quantity, coffee_quantity, amount_sold: Global variables tracking the machine's resources and sales.
Usage:
Run the script and follow the prompts to order drinks, view reports, or turn off the machine.'''
       

water_quantity = 500   #variable have been assigned to act as the container containing the ingredientd in the cooffe machine
milk_quantity = 250
coffee_quantity = 150
amount_sold = 0.00

def purchase(drink):  
        """Function set for purchase so as to enable user perform transactions on the coffe machine 
            with parameter 'drink' which takes as argument dictionary containg different coffee_types, (water, coffee, milk) quantity needed for production
        """
        global water_quantity  #calling the varaibles a global varaible so we can be able to modify them
        global milk_quantity
        global coffee_quantity
        global amount_sold
        #

        if water_quantity < drink['water']:               #condition set to verify if resources are still enough to process each command if not it returns the unsuficient resource
            return 'sorry there is not enough water.'
        elif milk_quantity < drink['milk']:
            return 'sorry there is not enough milk'
        elif coffee_quantity < drink['coffee']:
            return 'sorry there is not enough coffee'
        else:
            print('')
        #

        print('please insert coins. ')                    #input to get user payment
        quarters = float(input('How many Quarters?: '))
        dimes = float(input('How many Dimes?: '))
        nickles = float(input('How many nickles: '))
        pennies = float(input('How many pennies?: '))
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)   #suming up user payment 
        #

        if total >= drink['price']:   #condition set to evalaute if user cash is suficient for the purchase machine refunds users money
            amount_sold += total       #increment amount sold to sum up users purchases
            water_quantity -= drink['water']  #decrement resources based on quantity used to produce each user command
            milk_quantity-=drink['milk']
            coffee_quantity-=drink['coffee']
            print(f'Here is {(total - drink['price']):.2f}$ of your change')  #return users change
            return f'Here is your  {drink['coffee_type']}☕ enjoy' #whising user
        else:
            return 'Sorry thats not enough money refund !!'  #if user cash is insuficient system refunds users money
        #

def report():
    """function set to report status of machine resources"""
    print(f'Water : {water_quantity} \n MILK : {milk_quantity} \n COFFEE : {coffee_quantity} \n amount sold : {amount_sold}')

#   
cappucino = {'coffee_type':'Cappucino','water':250, 'coffee':24,'milk': 100, 'price' : 3.00}  #cappucino dictionary
expresso = {'coffee_type':'expresso','water':50, 'coffee':18,'milk': 0, 'price' : 1.50}   #expresso dictionary
latte = {'coffee_type':'latte','water':200, 'coffee':24,'milk': 150, 'price' : 2.50}   #latte dictionary


#TODO
def system():
    """funcdtion set to loop through machine functionalities until its resources are depleted"""
    proceed = True #intialization of while loop
    while proceed == True:  
        user_input = input('what should i save you : (expesso,latte,cappucino)').lower()  #getting user input
        if user_input == 'expresso':
            print(purchase(expresso))  #if user input is expresso we call the purchase() function and pass it the expresso dictionary as argument
        elif user_input == 'latte':
            print(purchase(latte))         #if user input is latte we call the purchase() function and pass it the latte dictionary as argument
        elif user_input == 'cappucino':
            print(purchase(cappucino))     #if user input is cappucino we call the purchase() function and pass it the cappucino dictionary as argument
        elif user_input == 'report':
            report()  #if user input is report we call the report() function
        elif user_input == 'off':     #if input if off the we switch of the system
            return 'Thanks for using the program!!' #return value of the function
        else:
            print('enter decision properly :')  #fault tolerane
print(system())  #printing the system() function to call it
