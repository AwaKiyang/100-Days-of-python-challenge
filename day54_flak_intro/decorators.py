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

"""Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output: 
You called a_function(1,2,3) 
It returned: 6 
The value 6 is the return value of the function.
Don't change the body of a_function. 
IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise. 
"""

#solution

def logging_decorator(func):
    # Define a wrapper that accepts any number of positional arguments
    def wrapper(*args):
        print(f'You called {func.__name__}{args}')  # Print the function name and arguments
        print(f'It returned : {func(*args)}')       # Print the return value of the function
        return func(*args)                          # Return the result of the function call
    return wrapper                                  # Return the wrapper function

@logging_decorator
def a_function(*args):
    return sum(args)                                # Return the sum of all arguments

a_function(1,2,3)                                   # Call the decorated function with arguments