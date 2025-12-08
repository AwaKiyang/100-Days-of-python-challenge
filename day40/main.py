
from update_sheet import update_google_sheet
from searching_flight import searching_flight
import smtplib

#--------------------Call if you want to update you spreadsheet information-----------------#

'''update_google_sheet().update_sheety_sheet()'''

# -------------------------------------------------------------- #
#   LOAD GOOGLE SHEET FLIGHT DATA
#   This retrieves the list of cities and their lowest price
#   from your Google Sheet via Sheety API.
#   It returns a dictionary that contains the "prices" list.
# -------------------------------------------------------------- #
cities_google_data = update_google_sheet().spreadsheet_data()['prices']


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

            my_email = "awakiyang9@gmail.com"
            password = "jtry lvtb oaog qckl"   # App Password for Gmail
            user_email_list = update_google_sheet().user_email()

            for user_email in user_email_list:
                try :
                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.starttls()
                        smtp.login(user=my_email, password=password)

                        subject = 'Cheap Flight'
                        body = f"Getting flight for {city_info['city']}...., price is lower {destination['minimum_price']} instead of {city_info['lowestPrice']}"

                        message = f"Subject: {subject}\n\n{body}"

                        smtp.sendmail(
                            from_addr=my_email,
                            to_addrs=user_email,
                            msg=message
                        )
                except Exception as e:
                    print('invalid email')
    
        else:
            print('sorry no flight found')

    except Exception as e:
        # Print any unexpected error during flight search
        print(f'the progam has ended')

        