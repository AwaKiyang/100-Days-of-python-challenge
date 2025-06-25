#creating a coffe machine
"""
expresso: 
    water: 50ml
    coffe: 18g
    milk : 0ml
    price : 1.50$
latte: 
    coffee : 24g
    water : 200ml
    milk : 150
    price : 2.50$
cappucino
    coffee : 24g
    water : 250ml
    milk : 100ml
    price: 3.00$

"""
class coffee_machine:
    def __init__(self,coffee_type, water, coffee, milk,price):
        self.coffee_type = coffee_type   
        self.water_quantity = water
        self.coffee_quatity = coffee
        self.milk_quantity = milk
        self.price = price

    def choice(self):
        return f'you have chosen {self.coffee_type} which is composed of \nwater : {self.water_quantity}ml\
        \nMIlk : {self.milk_quantity}ml \nCoffee : {self.coffee_quatity}grams \nPrice : {self.price:.2f}'
    def purchase(self):
        #
        print('please insert coins. ')
        quarters = int(input('How many Quarters?: '))
        dimes = int(input('How many Dimes?: '))
        nickles = int(input('How many nickles: '))
        pennies = int(input('How many pennies?: '))
        total = quarters+dimes+nickles+pennies
        if total < self.price:
            print('Sorry thats not enough money refund !!')
        else:
            print(f'Here is {(self.price - total):.2f} in change')
        #

expresso = coffee_machine('expresso',50,18,0,1.50)
latte = coffee_machine('latte',200,24,150,2.50)
cappucino = coffee_machine('Cappucino',250,24,100,3.00)
#
user_input = input('what should i save you : (expesso,latte,cappucino)').lower()
proceed = True
while proceed == True:
    if user_input == 'expesso':
        expresso.choice()
    elif user_input == 'latte':
        latte.choice()
    elif user_input == 'cappuccino':
        cappucino.choice()
    elif user_input == 'report':
        print(f'Water : {}')