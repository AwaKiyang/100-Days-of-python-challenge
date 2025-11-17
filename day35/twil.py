"""
Weather Alert SMS System

This script checks the weather forecast using OpenWeatherMap's 5-day/3-hour API.
If rain is expected in the next few forecast periods, a notification SMS is sent
via the Twilio API.

APIs used:
- OpenWeatherMap Forecast API: https://api.openweathermap.org/data/2.5/forecast
- Twilio SMS API: https://www.twilio.com/

Logic:
1. Fetch the next 4 forecast entries (~12 hours).
2. If any weather condition code < 700 → rain/snow/drizzle/storm detected.
3. Send an SMS alert using Twilio.
"""

import requests
from twilio.rest import Client

# Twilio account details (use environment variables in real apps)
account_sid = 'AC77c24b2911e64b9baaeed6505eacbe01'
auth_token = '039bae95483662b8a5c0a38ae9f2a0f8'

# OpenWeatherMap forecast endpoint
owm = "https://api.openweathermap.org/data/2.5/forecast"

# API request parameters
parameters = {
    'lat': 3.814616,       # Your latitude
    'lon': 11.453652,      # Your longitude
    'appid': '508f22bb53034b714f58acec1ba03908',  # API key
    'units': 'metric',     # Units in Celsius
    "cnt": 4               # Number of forecast entries to check (4 x 3hr = 12 hours)
}

# Make API request
weather_response = requests.get(owm, params=parameters)
weather_response.raise_for_status()

try:
    is_rainy = False

    # Loop through each forecast time block
    for forecast in weather_response.json()['list']:
        # Weather condition codes < 700 indicate rain/snow/drizzle/storm
        if forecast['weather'][0]['id'] < 700:
            is_rainy = True

    # If rain is expected, send an SMS alert
    if is_rainy:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+15013827337',              # Twilio sender number
            body='Get your umbrella — it will rain today!',
            to='+237652669338'                 # Your phone number
        )

        print(message.sid, "message sent")

except Exception as e:
    print(f"Sorry, we encountered an error: {e}")

finally:
    print("Process completed.")


"""
NB : storing you apikeys like this in your code is very risky since someone can just copy an use
    so in day 36 we will to to store our api keys and passwords in your machine for your own personal use 
    1 using .env file were we are going to store or api keys, secrets and others and then using the python-dotenv and os module to retrieve them
    2 storing them as environment variables and retriving them using the os module
"""