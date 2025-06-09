#creating a band name genrator which wiil generate a random band name
"""
This script generates a band name by combining the name of the city the user grew up in and the name of their pet.

Workflow:
1. Greets the user with a welcome message.
2. Prompts the user to input the name of the city they grew up in.
3. Prompts the user to input the name of their pet.
4. Outputs a suggested band name by concatenating the city and pet names.

Example:
    Welcome to the band name generator.
    What the name of the city you grew up in : Paris
    What is pets name : Max
    your band name is Paris Max
"""
print("Welcome to the band name generator.")
city = input('What the name of the city you grew up in : ')
pet = input('What is pets name : ')
print(f'your band name is {city} {pet}')
