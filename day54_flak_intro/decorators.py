'''
A decorator is a function that extends the behaviour of another function with or without modifying the base function
'''


# Define a decorator function that takes another function as input
def add_sprinkles(func):
    # Define a wrapper function that adds extra behavior
    def wrapper():
        print("you add sprinkels")  # Print message before calling the original function
        return func()  # Call the original function
    return wrapper  # Return the wrapper function

# Use the decorator to extend the behavior of get_ice_cream
@add_sprinkles
def get_ice_cream():
    print(f"here is your  ice cream")  # Print message for serving ice cream

# Call the decorated function
get_ice_cream()


"""Example 2 """
'''
@add_sprinkles
def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream")  # Print message for serving ice cream

# Call the decorated function
get_ice_cream('vanila')
'''   #if your run this you will get an error because by default a wrapper function is'nt set to recieve argument so to mitigate this you will use paratermer of *args and **kwargs on the wrapper funtion 
       #to accept any number of arguments and keyword arguments

def add_fudge(func):
    # Define a wrapper that accepts any arguments and keyword arguments
    def wrapper(*args, **kwargs):
        print('fudge is been added')  # Print message before calling the original function
        return func(*args, **kwargs)  # Call the original function with all arguments
    return wrapper  # Return the wrapper function

@add_fudge
def get_ice_fudge(flavour):
    print(f'get you {flavour} fudge on the ice cream')  # Print message for serving ice cream with fudge

get_ice_fudge('vanila')  # Call the decorated function with a flavor argument
