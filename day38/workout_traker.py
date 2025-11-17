import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

ACTIVITY = input("what activity did you do : ")
WEIGTH = int(input("what is your weight in pounds : "))
DURATION = input("how long have you been doing the exercise : ")

CALORIES_CALC_ENDPOINT = "https://calories-burned-by-api-ninjas.p.rapidapi.com/v1/caloriesburned"
SHEETY_ENDPOINT = "https://api.sheety.co/6428f16d9a6d7a7bb19162e551c723d3/copyOfMyWorkouts/workouts"

querystring = {
    "activity": ACTIVITY,
    "weight" : WEIGTH,
    "duration" : DURATION
    }

headers = {
	"x-rapidapi-key": os.getenv("x-rapidapi-key"),
	"x-rapidapi-host": "calories-burned-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url=CALORIES_CALC_ENDPOINT, headers=headers, params=querystring)
exercise_results = response.json()

try:
    date = datetime.now().strftime('%d/%m/%Y')
    time = datetime.now().strftime('%X')
    
    headers = {
        'Authorization' : os.getenv('Authorization')
    }
    for results in exercise_results:
        
        sheety_results = {
            'workout' : {
                'date' : date,
                'time' : time,
                'exercise' : results['name'].title(),
                'duration' : results['duration_minutes'],
                'calories' : results['total_calories']
            }
        }

        sheet_reponse = requests.post(url=SHEETY_ENDPOINT, json=sheety_results, headers=headers)
        print(sheet_reponse.text)
        print('google sheet updated')
except Exception as e:
    print(e)



