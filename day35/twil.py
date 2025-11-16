import requests
from twilio.rest import Client

account_sid = 'AC77c24b2911e64b9baaeed6505eacbe01'
auth_token = '039bae95483662b8a5c0a38ae9f2a0f8'

owm = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    'lat': 3.814616,
    'lon': 11.453652,
    'appid': '508f22bb53034b714f58acec1ba03908',
    'units': 'metric',
    "cnt" : 4
}

weather_response = requests.get(owm, params=parameters)
weather_response.raise_for_status()
try: 
    is_rainy = False
    for weathers in weather_response.json()['list']:
        if weathers['weather'][0]['id'] < 700:
            is_rainy = True

    if is_rainy:

        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='+15013827337',
        body='Get your umbrella today will be rain damy',
        to='+237652669338'
        )
        print(message.sid, "message sent")

except Exception as e:
    print(f'sorry we encounter an error {e}')
finally:
    print('nice try')