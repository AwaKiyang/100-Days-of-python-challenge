"""
ISS Overhead Notifier

This script checks two conditions:
1. The International Space Station (ISS) is within ±5 degrees of your location.
2. It is nighttime at your location.

If both conditions are true, the script sends an email notification.

APIs used:
- ISS current position: http://api.open-notify.org/iss-now.json
- Sunrise/Sunset times: https://api.sunrise-sunset.org/json
"""

import requests
import datetime
import smtplib

# Your coordinates
my_lat = 3.814616
my_long = 11.453652


def Iss_overhad():
    """
    Checks whether the ISS is currently within 5 degrees
    of both latitude and longitude of your location.

    Returns:
        True if ISS is overhead, otherwise False.
    """
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_longitude = float(iss_response.json()["iss_position"]["longitude"])
    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])

    # Check proximity within ±5 degrees
    if my_long - 5 <= iss_longitude <= my_long + 5 and my_lat - 5 <= iss_latitude <= my_lat + 5:
        return True
    return False


def is_night():
    """
    Determines whether it is currently nighttime at your location.

    API returns sunrise/sunset in UTC, so the comparison is done using UTC hour.

    Returns:
        True if it's nighttime (after sunset OR before sunrise),
        otherwise False.
    """
    params = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0  # ensures the API returns full ISO timestamps
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()

    data = response.json()["results"]

    sunrise_hour = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["sunset"].split("T")[1].split(":")[0])

    # Get current hour in UTC
    current_hour = datetime.datetime.utcnow().hour

    # Nighttime if current time is after sunset OR before sunrise
    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    return False


# ------------------- MAIN EXECUTION ------------------- #
# If ISS is overhead AND it's nighttime, send an email
if Iss_overhad() and is_night():

    my_email = "awakiyang9@gmail.com"
    password = "jtry lvtb oaog qckl"   # App Password for Gmail

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(user=my_email, password=password)

        subject = 'ISS is overhead!'
        body = 'Go outside and look up — the ISS is passing above your location right now.'

        message = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(
            from_addr=my_email,
            to_addrs="awakiyang9@gmail.com",
            msg=message
        )
