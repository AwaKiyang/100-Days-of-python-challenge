#today we are going to create an auction program to collect user bids and store in a dictionary and then proceed to return user with the higest bid
"""
This script implements a simple auction program that collects user bids and determines the highest bidder.
Functions:
    users():
        Prompts the user for their name and bid amount, then appends this information as a dictionary to the global 'biders' list.
    auction():
        Sorts the 'biders' list in descending order based on the bid amount and returns a string announcing the user with the highest bid.
Workflow:
    - The program starts by collecting the first user's bid.
    - It then enters a loop, repeatedly asking if more users want to bid.
    - If the user chooses "yes", it collects another bid.
    - If the user chooses "no", the loop ends.
    - Finally, the program announces the user with the highest bid.
"""
print('welcome with ur bidding program you can now proceed with bid')
print("""
                          /
                  )_______(
                  |"""""""|_.-._,.---------.,_.-._
                  |       | | |               | | ''-.
                  |       |_| |_             _| |_..-'
                  |_______| '-'''---------'' '-'
                  )"""""""(
                 /_________\\
               .-------------.
              /_______________\\
""")

biders = list() #biders list to store an array of dictionaries each containing username and bid 

def users(): #function users for collecting username and bid then pushing it to biders list
    username = input("what is your name : $") #input to collect user name
    bid = int(input("what is your bid : $")) #input to collect user bid
    biders.append({"user" : username, "price" : bid})  #appending username and bid as dictionary in biders list
users()

proceed = True #intailization of while loop
while proceed == True: #condition set to true 
    deccision = input("would you like to continue \"yes\" or \"no\" : ").lower() #decissioin to continue bid with two options yes or no
    if deccision == "yes": #if yes we recall users() and proceed
        print("okay lets continue")
        print("\n" * 100) #print next line a hundred times
        users()  
    elif deccision == "no": #if no we set proceed to false and end the while loop
        proceed = False
    else:
        print("enter deccision correctly :") #enter deccision properly
        
def auction():   #function to query through biders array of dictionaries and select user with the higest bid
    biders.sort(key=lambda user : user["price"],reverse=True) #sort method associated with lambda funtion to sort according to price in desending order
    return f'the user {biders[0]["user"]} has the highest bid of {biders[0]["price"]}$' #return username with the highest bid

print(auction()) 



