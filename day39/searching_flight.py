import requests
from amadues_token_generator import amadues_token
from datetime import datetime, timedelta

# -------------------------------------------------------------- #
# CLASS: searching_flight
# This class handles:
#   - Creating a flight search request to Amadeus API
#   - Searching for round-trip flight offers
#   - Returning the cheapest flight found
# -------------------------------------------------------------- #
class searching_flight:

    def __init__(self, cities_iata):
        # ------------------------------------------------------ #
        # Set travel date range:
        #   - Departure: 1 day from today
        #   - Return: 180 days from today
        # ------------------------------------------------------ #
        self.from_time = datetime.now() + timedelta(days=1)
        self.to_time = datetime.now() + timedelta(days=180)

        # Flight search endpoint for Amadeus API
        self.fligth_search_endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

        # Generate a fresh access token for authentication
        self.auth_token = amadues_token().get_token()

        # Authorization header containing Bearer token
        self.headers = {
            'Authorization': f'Bearer {self.auth_token}'
        }

        # ------------------------------------------------------ #
        # Parameters for the flight search:
        #   - originLocationCode: hardcoded as LON (London)
        #   - destinationLocationCode: provided by user (IATA code)
        #   - Dates: formatted as YYYY-MM-DD
        #   - Adults: 1 traveler
        #   - nonStop: only direct flights
        #   - currencyCode: price returned in USD
        #   - max: limit results to 10 flights
        # ------------------------------------------------------ #
        self.parameter = {
            "originLocationCode": 'LON',
            "destinationLocationCode": cities_iata,
            "departureDate": self.from_time.strftime("%Y-%m-%d"),
            "returnDate": self.to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": "10",
        }

    # -------------------------------------------------------------- #
    # METHOD: fligth_search
    # Sends the request to Amadeus, receives flight data,
    # extracts the cheapest result, and returns a dictionary:
    #   { origin, destination, out_date, return_date, minimum_price }
    # -------------------------------------------------------------- #
    def fligth_search(self):

        # Send GET request to Amadeus flight search API
        fligth_search_reponse = requests.get(
            url=self.fligth_search_endpoint,
            headers=self.headers,
            params=self.parameter
        )

        # Parse JSON response
        flight_info = fligth_search_reponse.json()



        try:
            # Ensure flights were found
            if flight_info['meta']['count'] != 0:

                # Extract all flight prices
                price_list = [
                    float(fees['price']['grandTotal'])
                    for fees in flight_info['data']
                ]

                # Find the minimum price
                minimum_price = min(price_list)

                # Dictionary to store the cheapest flight found
                cheapest_flight = dict()

                # Loop through flights to match the cheapest offer
                for flight in flight_info['data']:
                    if float(flight['price']['grandTotal']) == minimum_price:
                        origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                        destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                        out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                        return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

                        # Build dictionary for cheapest flight
                        cheapest_flight = {
                            'origin': origin,
                            'destination': destination,
                            'out_date': out_date,
                            'return_date': return_date,
                            'minimum_price': minimum_price
                        }
                return cheapest_flight
            
        except Exception as e:
            # Handles unexpected data errors
            print(f"sorry we ecountered an error {e}")

        
