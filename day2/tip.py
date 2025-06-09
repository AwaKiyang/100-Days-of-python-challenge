#today we we will build a tip calculator which will wnwable customer to equally split thier bill
"""
A simple tip calculator that splits the total bill among a group of people, including a specified tip amount.

Workflow:
1. Prompts the user to enter the total bill amount.
2. Asks the user for the desired tip amount (e.g., 12, 15, or 2).
3. Requests the number of people sharing the bill.
4. Calculates and displays the amount each person should pay, including their share of the tip.

Note:
- The tip is added as a fixed amount per person, not as a percentage of the bill.
- All inputs are expected to be integers.
"""
print('******welcome to tip calculator*****\n')
total = int(input('What was the total bill : $'))
tip = int(input('how much would you like to tip is it 12 , 15 or 2: $'))
persons = int(input('how many poeple will pay the bill : '))
print(f'Each person should pay : {((total/persons)+tip):.2f}$')
