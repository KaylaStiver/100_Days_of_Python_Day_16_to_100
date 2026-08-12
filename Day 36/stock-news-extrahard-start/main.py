import requests_cache
import datetime
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def check_stock():
    #Cached session of stock API to reduce num of requests. Expires after 3600s.
    tsla_stock = requests_cache.CachedSession("tsla_cache", expire_after=3600)

    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': AV_API_KEY
    }

    response = tsla_stock.get("https://alphavantage.co/query", params=params)
    response.raise_for_status()
    tsla_data = response.json()

    #Retrieving yesterday and today's date and reformatting dates for dict keys
    today = datetime.date.today()
    today_format = today.strftime("%Y-%m-%d")

    yesterday = today - datetime.timedelta(days=1)
    yesterday_format = yesterday.strftime("%Y-%m-%d")

    #Fetching yesterday and today's closing price
    today_price = tsla_data["Time Series (Daily)"][today_format]["4. close"]
    yesterday_price = tsla_data["Time Series (Daily)"][yesterday_format]["4. close"]

    #Calculating difference between closing prices as a percentage
    price_diff = abs(today_price - yesterday_price) / ((today_price + yesterday_price) / 2) * 100

    #If a 5% differential is reached, stock news need to be gathered.
    if price_diff <= 5:
        print("Get News")

check_stock()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


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

