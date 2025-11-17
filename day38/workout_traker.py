
"""
This script tracks a user's workout activity, calculates calories burned using the Calories Burned API, 
and logs the workout details to a Google Sheet via the Sheety API.
Workflow:
1. Prompts the user for activity type, weight (in pounds), and duration of exercise.
2. Sends a GET request to the Calories Burned API to retrieve calories burned for the specified activity.
3. Formats the current date and time.
4. For each result returned by the API, constructs a payload containing workout details.
5. Sends a POST request to the Sheety API to log the workout in a Google Sheet.
6. Handles exceptions and prints error messages if any occur.
Environment Variables:
- x-rapidapi-key: API key for Calories Burned API.
- Authorization: Bearer token for Sheety API.
Dependencies:
- requests
- datetime
- os
- dotenv
User Inputs:
- Activity performed
- Weight in pounds
- Duration of exercise
API Endpoints:
- Calories Burned API (GET): Calculates calories burned based on activity, weight, and duration.
- Sheety API (POST): Logs workout details to a Google Sheet.
Output:
- Prints the response from the Sheety API and confirms the Google Sheet update.
- Prints error messages if exceptions occur.
"""
import requests  # Import the requests library for making HTTP requests
from datetime import datetime  # Import datetime for handling date and time
import os  # Import os for accessing environment variables
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

# Prompt the user to enter the activity performed
ACTIVITY = input("what activity did you do : ")
# Prompt the user to enter their weight in pounds and convert it to integer
WEIGTH = int(input("what is your weight in pounds : "))
# Prompt the user to enter the duration of the exercise
DURATION = input("how long have you been doing the exercise : ")

# API endpoint for calculating calories burned
CALORIES_CALC_ENDPOINT = "https://calories-burned-by-api-ninjas.p.rapidapi.com/v1/caloriesburned"
# API endpoint for logging workout details to Google Sheet via Sheety
SHEETY_ENDPOINT = "https://api.sheety.co/6428f16d9a6d7a7bb19162e551c723d3/copyOfMyWorkouts/workouts"

# Query parameters for the Calories Burned API
querystring = {
    "activity": ACTIVITY,
    "weight" : WEIGTH,
    "duration" : DURATION
}

# Headers for the Calories Burned API request, including API key and host
headers = {
    "x-rapidapi-key": os.getenv("x-rapidapi-key"),
    "x-rapidapi-host": "calories-burned-by-api-ninjas.p.rapidapi.com"
}

# Send GET request to Calories Burned API and get the response
response = requests.get(url=CALORIES_CALC_ENDPOINT, headers=headers, params=querystring)
# Parse the JSON response to get exercise results
exercise_results = response.json()

try:
    # Get the current date in DD/MM/YYYY format
    date = datetime.now().strftime('%d/%m/%Y')
    # Get the current time in HH:MM:SS format
    time = datetime.now().strftime('%X')
    
    # Headers for Sheety API request, including Authorization token
    headers = {
        'Authorization' : os.getenv('Authorization')
    }
    # Iterate over each result returned by the Calories Burned API
    for results in exercise_results:
        # Construct the payload with workout details for Sheety API
        sheety_results = {
            'workout' : {
                'date' : date,
                'time' : time,
                'exercise' : results['name'].title(),
                'duration' : results['duration_minutes'],
                'calories' : results['total_calories']
            }
        }

        # Send POST request to Sheety API to log the workout
        sheet_reponse = requests.post(url=SHEETY_ENDPOINT, json=sheety_results, headers=headers)
        # Print the response from Sheety API
        print(sheet_reponse.text)
        # Confirm that the Google Sheet has been updated
        print('google sheet updated')
except Exception as e:
    # Print any exception that occurs during the process
    print(e)
