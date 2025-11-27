
from update_sheet import update_google_sheet
from searching_flight import searching_flight
from twilio.rest import Client
import os
# Twilio account credentials
account_sid = 'AC77c24b2911e64b9baaeed6505eacbe01'
auth_token = os.getenv('auth_token')  #auth_token was the environmetn variable stored in our system which is the api key of our twliio account

#--------------------Call if you want to update you spreadsheet information-----------------#

'''update_google_sheet().update_sheety_sheet()'''

# -------------------------------------------------------------- #
#   LOAD GOOGLE SHEET FLIGHT DATA
#   This retrieves the list of cities and their lowest price
#   from your Google Sheet via Sheety API.
#   It returns a dictionary that contains the "prices" list.
# -------------------------------------------------------------- #
cities_google_data = update_google_sheet().spreadsheet_data()
print(cities_google_data)

# -------------------------------------------------------------- #
#   LOOP THROUGH EACH CITY IN THE SHEET
#   For every city:
#       - Retrieve its IATA code (already in the sheet)
#       - Search for flights using your searching_flight class
#       - Compare the minimum price returned by Amadeus
#         with the stored "lowestPrice" in your Google Sheet.
#       - Print a message if the new price is cheaper.
# -------------------------------------------------------------- #
for city_info in cities_google_data:
    try:
        # ------------------------------------------- #
        # Create a new flight search object using the
        # IATA code stored in your Google Sheet.
        # ------------------------------------------- #
        destination_city = searching_flight(cities_iata=city_info['iataCode'])

        # Perform the actual flight search request
        destination = destination_city.fligth_search()

        # ------------------------------------------- #
        # Compare Amadeus flight price vs Google Sheet
        # lowestPrice value.
        # ------------------------------------------- #
        if destination['minimum_price'] < city_info['lowestPrice']:
            '''print(
                f" Getting flight for {city_info['city']}...., "
                f"price is lower {destination['minimum_price']} instead of {city_info['lowestPrice']}"
            )'''
            
            client = Client(account_sid, auth_token)
            # Send SMS with flight price change, headline, and brief
            message = client.messages.create(
                from_='+15013827337',
                body=f"price is lower {destination['minimum_price']} instead of {city_info['lowestPrice']}",
                to='+237652669338'
            )
            print(message.sid)  # Print message SID for confirmation

        else:
            print('sorry no flight found')

    except Exception as e:
        # Print any unexpected error during flight search
        print(f'{e}')
