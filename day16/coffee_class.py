"""
Coffee Machine Simulation

This script simulates a coffee vending machine that can serve three types of coffee drinks: espresso, latte, and cappuccino.
It manages resources (water, milk, coffee) and tracks the total amount sold. The user can interact with the machine via a command-line interface to purchase drinks, check the machine's resource report, or turn off the machine.

Features:
- Resource Management: Tracks the quantities of water, milk, and coffee in the machine.
- Drink Selection: Supports espresso, latte, and cappuccino, each with specific resource requirements and prices.
- Payment Handling: Accepts coin input (quarters, dimes, nickels, pennies), calculates total payment, and provides change if necessary.
- Reporting: Allows the user to view the current status of resources and total sales.
- Shutdown: The machine can be turned off by the user.

Classes:
    coffee_machine:
        Represents a coffee drink type with its required resources and price.
        Methods:
            __init__(self, coffee_type, water, coffee, milk, price):
                Initializes a coffee drink with its name, required water, coffee, milk, and price.
            purchase(self):
                Handles the purchase process, including resource checking, payment input, transaction validation, and updating resources.

Functions:
    report():
        Returns a string reporting the current status of the machine's resources and total amount sold.

Global Variables:
    water_quantity (int): Current amount of water in the machine (ml).
    milk_quantity (int): Current amount of milk in the machine (ml).
    coffee_quantity (int): Current amount of coffee in the machine (g).
    amount_sold (float): Total money collected from sales.

Usage:
    - The user is prompted to select a drink (espresso, latte, cappuccino), request a report, or turn off the machine.
    - For drink purchases, the machine checks if enough resources are available, processes coin input, and dispenses the drink if payment is sufficient.
    - The machine can be turned off by entering 'off'.

Drink Recipes:
    espresso: 
        water: 50ml
        coffee: 18g
        milk: 0ml
        price: $1.50
    latte: 
        water: 200ml
        coffee: 24g
        milk: 150ml
        price: $2.50
    cappuccino:
        water: 250ml
        coffee: 24g
        milk: 100ml
        price: $3.00
tank_capacity:
    water_quantity = 500   #variable have been assigned to act as the container containing the ingredientd in the cooffe machine
    milk_quantity = 250
    coffee_quantity = 150
    amount_sold = 0.00
"""
#
water_quantity = 500   #variable have been assigned to act as the container containing the ingredientd in the cooffe machine
milk_quantity = 250
coffee_quantity = 150
amount_sold = 0.00

def report():
    """function set to report status of machine resources"""
    return f'Water : {water_quantity} \n MILK : {milk_quantity} \n COFFEE : {coffee_quantity} \n amount sold : {amount_sold}'

class coffee_machine:  #creating a class to enable functioning with three diferent objects and thier respective values
    def __init__(self,coffee_type, water, coffee, milk,price):  #intializing the class
        self.coffee_type = coffee_type    #attaching object value to self parameter
        self.water_needed = water
        self.coffee_needed = coffee
        self.milk_needed = milk
        self.price = price

    def purchase(self): #method purchase which wil be ib charge of purchase processes
        """Handles the purchase process, including resource checking, payment input, transaction validation, and updating resources."""
        global water_quantity  #calling the varaibles a global varaible so we can be able to modify them
        global milk_quantity
        global coffee_quantity
        global amount_sold

        if water_quantity < self.water_needed:               #condition set to verify if resources are still enough to process each command if not it returns the unsuficient resource
            return 'sorry there is not enough water.'
        elif milk_quantity < self.milk_needed:
            return 'sorry there is not enough milk'
        elif coffee_quantity < self.coffee_needed:
            return 'sorry there is not enough coffee'
        else:
            print('')

        print('please insert coins. ')  
        try:                  #input to get user payment
            quarters = float(input('How many Quarters?: '))
            dimes = float(input('How many Dimes?: '))
            nickles = float(input('How many nickles: '))
            pennies = float(input('How many pennies?: '))
        except ValueError:    #using exception handlling in case user input is incorrect
            return 'Invalid input transaction cancelled'
        
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)   #suming up user payment 

        if total >= self.price:   #condition set to evalaute if user cash is suficient for the purchase machine refunds users money
            amount_sold += self.price       #increment amount sold to sum up users purchases
            water_quantity -= self.water_needed #decrement resources based on quantity used to produce each user command
            milk_quantity-= self.milk_needed
            coffee_quantity-= self.coffee_needed
            print(f'Here is {(total - self.price):.2f} of your change')  #return users change
            return f'Here is your  {self.coffee_type}☕ enjoy' #whising user
        else:
            return 'Sorry thats not enough money refund !!'  #if user cash is insuficient system refunds users money
        


expresso = coffee_machine('expresso',50,18,0,1.50)   #creating our objects with respectivr arguments to our class coffee_machine parameters
latte = coffee_machine('latte',200,24,150,2.50)
cappucino = coffee_machine('Cappucino',250,24,100,3.00)

#main loop
proceed = True
while proceed == True:
    user_input = input('what should i save you : (expresso,latte,capucino)').lower()    
    if user_input == 'expresso':
        print(expresso.purchase())   #if user_inpu is expresso we call the expresso object passing ti the purchase method
    elif user_input == 'latte':
        print(latte.purchase())         #if user_inpu is expresso we call the latte object passing ti the purchase method
    elif user_input == 'capucino':
        print(cappucino.purchase())      #if user_inpu is expresso we call the capucino object passing ti the purchase method
    elif user_input == 'report':
        print(report())               #if user input is report we call the report() function
    elif user_input == 'off':
        print('Thanks for using the Machine')    #if input if off the we switch oof the system
        proceed = False         #terminate the while loop
    else:
        print('Enter decision properly!!')