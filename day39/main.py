import requests
import os
from dotenv import load_dotenv
load_dotenv()

# ---------------------------- Sheety Setup ----------------------------- #
# This is the Sheety API endpoint that points to your Google Sheet
Sheety_Endpoint = 'https://api.sheety.co/6428f16d9a6d7a7bb19162e551c723d3/flightDeals/prices'

# Authorization token for Sheety (stored inside .env as "Authorization")
sheety_header = {
    'Authorization' : os.getenv('Authorization')
}

# Request the spreadsheet data
sheety_reponse = requests.get(url=Sheety_Endpoint)
spread_sheet_data = sheety_reponse.json()



# ---------------- Amadeus Token Generation Function ------------------ #
def get_token():
    """
    Generates an access token from the Amadeus API using client credentials.
    It sends a POST request with your API key and secret to obtain a Bearer token.
    """

    token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

    # Required headers for form-url-encoded request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # OAuth2 parameters for client credentials grant
    parameters = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('amadues-client-id'),
        'client_secret': os.getenv('amadues-secret')
    }
    
    # Send authentication request
    response = requests.post(token_endpoint, data=parameters, headers=headers)

    # Extract the access token from the JSON response
    auth_token = response.json()['access_token']
    return auth_token


# Print token to verify working
print(get_token())


# ----------------- Retrieve IATA Code from Amadeus API ---------------- #
def get_city_iataCode(city):
    """
    Takes a city name (e.g. 'Paris') and sends a request to the Amadeus
    city search API to retrieve the corresponding IATA code (e.g. 'PAR').
    """

    amadues_city_search_endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

    # Generate fresh access token
    auth_token = get_token()

    # Authorization header using the token
    headers = {
        'Authorization':f'Bearer {auth_token}'
    }

    # Parameters for city lookup
    parameters ={
        "keyword": city,
        'max' : 1
        }

    # Send search request and return the first result’s IATA code
    city_search_reponse = requests.get(url=amadues_city_search_endpoint, params=parameters, headers=headers)
    return city_search_reponse.json()['data'][0]['iataCode']



# ---------------------- Update Spreadsheet with IATA ------------------ #
def update_sheety_sheet():
    """
    Loops through each row in the Sheety spreadsheet.
    For every city found, it retrieves the IATA code from Amadeus
    and updates the Google Sheet via a PUT request.
    """

    try:

        for city_name in spread_sheet_data['prices']:

            # Build update endpoint for each row using its ID
            sheety_update_endpoint = f'https://api.sheety.co/6428f16d9a6d7a7bb19162e551c723d3/flightDeals/prices/{city_name['id']}'

            # Get IATA code for the city
            iatacode = get_city_iataCode(city_name["city"])

            # Sheety API expects data under a "price" object
            parameters = {
                'price' : {
                    'iataCode' : iatacode
                }
            }

            # Send update request to Sheety
            update_response = requests.put(url=sheety_update_endpoint, json=parameters)
            print(update_response.text)

    except Exception as e:
        # Catch and print any errors
        print(e)

# Execute the update function
update_sheety_sheet()
