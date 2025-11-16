import requests
from twilio.rest import Client

account_sid = 'AC77c24b2911e64b9baaeed6505eacbe01'
auth_token = '039bae95483662b8a5c0a38ae9f2a0f8'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

stock_api_parameters = {
    'symbol' : STOCK,
    'interval' : '1day',
    'apikey' : "0627d198354d44bca010bfee5f1f69d2",
    'outputsize' : 2
}
news_api_parameters = {
    'apikey' : 'pub_0a45a0122fb34ee2b391eab8e2aa6708',
    'country' : 'us',
    'language' : 'en',
    'symbol' : STOCK,
    'size' : 3
}
STOCK_URL = 'https://api.twelvedata.com/time_series'
NEWS_URL = 'https://newsdata.io/api/1/market'

stock_response = requests.get(STOCK_URL, params=stock_api_parameters)
data = stock_response.json()

news_reponse = requests.get(NEWS_URL, params=news_api_parameters)
news = news_reponse.json()


def percentage():
    yesterday_closing = float(data['values'][0]['close'])
    before_yesterday_closing = float(data['values'][1]['close'])
    price_change = yesterday_closing - before_yesterday_closing
    percentage_change = (price_change / before_yesterday_closing) * 100

    if percentage_change > 0:
        return f'TSLA: 🔺{percentage_change:.3f}%'
    else:
        return f'TSLA: 🔻{percentage_change:.3f}%'

rise = percentage()

def get_news():
    for news_article in news["results"]:
        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            from_='+15013827337',
            body=f'{rise} \n Headline: {news_article['title']} \n Brief: {news_article["description"]}',
            to='+237652669338'
            )
            print(message.sid)
        except Exception as e:
            print(f'sorry we could not send you message because of {e}')
get_news()
        







     
    
## STEP 2: Use 

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

