"""
Stock & News SMS Alert System (main.py)

Summary:
--------
This script monitors Tesla Inc. (TSLA) stock price movements and sends SMS alerts
containing recent news headlines using Twilio.

How It Works:
-------------
1. Fetch TSLA stock data (last 2 days) from the Twelve Data API.
2. Calculate the percentage change between yesterday's and the previous day's closing prices.
3. Fetch the top 3 recent news articles related to TSLA from NewsData.io.
4. Send an SMS for each news article using Twilio, including:
       - Stock price movement (UP 🔺 or DOWN 🔻)
       - News headline
       - Short description

Purpose:
--------
Automates real-time financial monitoring and delivers instant stock movement
and news alerts via SMS.

Dependencies:
-------------
- requests           → For API calls
- twilio.rest.Client → For sending SMS alerts

APIs Used:
-----------
1. Twelve Data API  → Stock price time series
2. NewsData.io      → Financial and market-related news
3. Twilio SMS API   → Sending notifications
"""

import requests
from twilio.rest import Client
import os   # import the os module so as to be able to get environment variable stored in our system
from dotenv import load_dotenv #used with os module in other to access variable stored in our .env file
load_dotenv()

# Twilio account credentials
account_sid = 'AC77c24b2911e64b9baaeed6505eacbe01'
auth_token = os.getenv('auth_token')  #auth_token was the environmetn variable stored in our system which is the api key of our twliio account

STOCK = "TSLA"  # Stock symbol
COMPANY_NAME = "Tesla Inc"  # Company name

# Parameters for stock API request
stock_api_parameters = {
    'symbol' : STOCK,
    'interval' : '1day',
    'apikey' : os.getenv('stocksApikey'), #this is the api key of our stock api_endpoint which was stored in our .env file and called using the os module and  dot-env.load_dotenv() method
    'outputsize' : 2  # Get last 2 days of data
}

# Parameters for news API request
news_api_parameters = {
    'apikey' : os.getenv('newsApikey'), #this is the api key of our news api_endpoint which was stored in our .env file and called using the os module and dot-env.load_dotenv() method
    'country' : 'us',
    'language' : 'en',
    'symbol' : STOCK,
    'size' : 3  # Get top 3 news articles
}

STOCK_URL = 'https://api.twelvedata.com/time_series'  # Stock API endpoint
NEWS_URL = 'https://newsdata.io/api/1/market'         # News API endpoint

# Fetch stock data
stock_response = requests.get(STOCK_URL, params=stock_api_parameters)
data = stock_response.json()
print(data)

# Fetch news data
news_reponse = requests.get(NEWS_URL, params=news_api_parameters)
news = news_reponse.json()

def percentage():
    """
    Calculates the percentage change in closing prices between yesterday and the day before.

    Returns:
        str: A formatted string indicating the percentage change in TSLA's closing price,
             prefixed with an up arrow (🔺) for positive change or a down arrow (🔻) for negative change.
    """
    # Get closing prices for yesterday and the day before
    yesterday_closing = float(data['values'][0]['close'])
    before_yesterday_closing = float(data['values'][1]['close'])
    # Calculate price change and percentage change
    price_change = yesterday_closing - before_yesterday_closing
    percentage_change = (price_change / before_yesterday_closing) * 100

    # Format the percentage change with an arrow
    if percentage_change > 0:
        return f'TSLA: 🔺{percentage_change:.3f}%'
    else:
        return f'TSLA: 🔻{percentage_change:.3f}%'

rise = percentage()  # Store formatted percentage change

def get_news():
    """
    Sends SMS notifications for each news article in the provided news results.

    Iterates through the news articles, initializes a Twilio client, and sends an SMS containing
    the stock change, headline, and brief description to a specified phone number. Prints the
    message SID upon successful sending, and prints an error message if sending fails.

    Raises:
        Exception: If there is an error during the SMS sending process.
    """
    # Loop through each news article in the results
    for news_article in news["results"]:
        try:
            # Initialize Twilio client
            client = Client(account_sid, auth_token)
            # Send SMS with stock change, headline, and brief
            message = client.messages.create(
                from_='+15013827337',
                body=f'{rise} \n Headline: {news_article["title"]}',
                to='+237652669338'
            )
            print(message.sid)  # Print message SID for confirmation
            print('  message deliverd')
        except Exception as e:
            # Print error if message sending fails
            print(f'sorry we could not send you message because of {e}')

get_news()  # Call function to send news SMS
