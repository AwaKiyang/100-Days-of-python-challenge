calco = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

"""
print(calco)  #calco string containing or ascii charater
def calculator():     
    """calculator function to proceed with arithmetic operations"""
    first_number = float(input("enter first number : "))   #collecting user input
    second_number = float(input("enter second number : "))
    print("\n+ : add\n/ : divide\n- : subtract\n* : multiply\n")  #print usable operations
    operation = input("Pick an operation : ")  #collecting users chosen opration

    if operation == "+":  # conditional to proceed with arithmetic operatins absed on user input
        print(f'{first_number} + {second_number} = {first_number+second_number}')
    elif operation == "-":
        print(f'{first_number} - {second_number} = {first_number-second_number}')
    elif operation == "*":
        print(f'{first_number} * {second_number} = {first_number*second_number}')
    elif operation == "/":
        print(f'{first_number} / {second_number} = {first_number/second_number}')
    else:
        print("enter operation properly")
calculator() #calling function

proceed = True  #initialins the while loop with proceed set to True
while proceed == True:  
    should_continue = input("would you like to continue \"yes\" or \"no\" : \n").lower() #collecting user input for continuation or stopage of program
    if should_continue == "yes": #if yes continue with code
        calculator()
    elif proceed == "no":  #if no proceed set to false an dwhile loop ends
        proceed = False
    else:
        print("Enter deciccision properly ===> ") 

fat32 = ""