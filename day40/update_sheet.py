import requests
import os
from amadues_token_generator import amadues_token
from dotenv import load_dotenv

load_dotenv()

# ---------------------------- Sheety Setup ----------------------------- #
class update_google_sheet:

    def __init__(self):
        # This is the Sheety API endpoint that points to your Google Sheet
        self.Sheety_Endpoint = 'https://api.sheety.co/d760ba2332a54176d5707cd4a6b33b2d/flightDeals/prices'

        # Authorization token for Sheety (stored inside .env as "Authorization")
        self.sheety_header = {
            'Authorization' : os.getenv('Authorization')
        }
        self.user_endpoint = 'https://api.sheety.co/d760ba2332a54176d5707cd4a6b33b2d/untitledSpreadsheet/sheet1'
        self.user_headers = {
            'Authorization' : os.getenv('userAuth')
        }

    def spreadsheet_data(self):
        # Request the spreadsheet data
        sheety_reponse = requests.get(url=self.Sheety_Endpoint)
        spread_sheet_data = sheety_reponse.json()
        return spread_sheet_data
    # ----------------- Retrieve IATA Code from Amadeus API ---------------- #
    
    def get_city_iataCode(self, city):
        """
        Takes a city name (e.g. 'Paris') and sends a request to the Amadeus
        city search API to retrieve the corresponding IATA code (e.g. 'PAR').
        """
        amadues_city_search_endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

        # Generate fresh access token
        auth_token = amadues_token().get_token()

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
    def update_sheety_sheet(self):
        """
        Loops through each row in the Sheety spreadsheet.
        For every city found, it retrieves the IATA code from Amadeus
        and updates the Google Sheet via a PUT request.
        """
        try:

            for city_name in self.spreadsheet_data()['prices']:

                # Build update endpoint for each row using its ID
                sheety_update_endpoint = f'https://api.sheety.co/d760ba2332a54176d5707cd4a6b33b2d/flightDeals/prices/[Object ID]/{city_name['id']}'

                # Get IATA code for the city
                iatacode = self.get_city_iataCode(city=city_name["city"])

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

    def user_email(self):
        user_get_reponse = requests.get(url=self.user_endpoint, headers=self.user_headers)
        user_sheet = user_get_reponse.json()
        return [email['email'] for email in user_sheet['sheet1']]
    
    def user_auth(self):

        user_email_list = self.user_email()  
        user_first_name = input('please enter your first name : ')
        user_last_name = input('please enter your last name : ')
        user_email = ''
        proceed = True
        while proceed == True:
            user_email = input('please enter your last email : ')
            if user_email not in user_email_list:
                proceed = False
                pass
            else:
                print('user email already exist enter another email')

        data = {
            'sheet1' : {
                'firstName' : user_first_name,
                'lastName' : user_last_name,
                'email' : user_email
            }
        }
        user_create = requests.post(url=self.user_endpoint, json=data)
        return user_create.text

# Execute the update function
#------------update_google_sheet().update_sheety_sheet()------#
