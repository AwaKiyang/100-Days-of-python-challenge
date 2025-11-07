import requests
import datetime
import smtplib
"""
some api's require some parameters which we must input
"""
my_lat = 3.814616
my_long = 11.453652


def Iss_overhad():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")

    iss_longitue = float(iss_response.json()["iss_position"]["longitude"])
    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
    if my_long-5 <= iss_longitue <= my_long+5 and my_lat-5 <= iss_latitude <= my_lat+5:
        return True 
    
def is_night():
    parameter = {
    "lat": my_lat,
    "lng": my_long
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()

    sunrise_time = int(response.json()["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset_time = int(response.json()["results"]["sunset"].split('T')[1].split(":")[0])
    time_now = datetime.datetime.now()

    if time_now <= sunset_time or time_now <= sunrise_time:
        return True

if Iss_overhad() and is_night():

    my_eamil = "awakiyang9@gmail.com"
    password = "jtry lvtb oaog qckl"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(user=my_eamil, password=password)

        subject = 'ISS is overhead'
        body= 'Common Iss is over you look to the sky and check it'

        message = f'Subject: {subject}\n\n {body}'
        smtp.sendmail(from_addr= my_eamil, to_addrs= 'awakiyang9@gmail.com', msg=message)  