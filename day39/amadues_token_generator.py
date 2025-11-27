import requests
import os
from dotenv import load_dotenv
load_dotenv()

# ---------------- Amadeus Token Generation Class ------------------ #
# This class is responsible for creating an OAuth2 access token
# required for all authenticated requests to the Amadeus API.
# It uses the Client Credentials authentication flow.
class amadues_token:

    def __init__(self):
        # token generation endpoint (Amadeus authentication URL)
        # This is where we send the POST request to obtain an access token.
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # Required headers for form-url-encoded POST request.
        # Amadeus API requires this content type for OAuth token generation.
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # OAuth2 parameters used in the client credentials grant.
        # These are loaded securely from the .env file:
        #  - client_id (your Amadeus API key)
        #  - client_secret (your Amadeus API secret)
        #  - grant_type must always be "client_credentials"
        self.parameters = {
            'grant_type': 'client_credentials',
            'client_id': os.getenv('amadues-client-id'),
            'client_secret': os.getenv('amadues-secret')
        }

    # ---------------------- Generate Token ------------------------ #
    def get_token(self):
        """
        Generates an access token from the Amadeus API using client credentials.

        Process:
        - Sends a POST request to the OAuth endpoint
        - Includes client_id, client_secret, and grant_type
        - Receives a JSON response containing an "access_token"
        - Returns the token as a string to be used in Authorization headers
        """
        # Send POST request to the token endpoint
        response = requests.post(
            url=self.token_endpoint,
            data=self.parameters,
            headers=self.headers
        )

        # Extract and return the access token from the JSON response
        auth_token = response.json()['access_token']
        return auth_token
