import os
import subprocess as sp; sp.call('cls', shell=True)
import requests
import datetime
import json
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ.get("alphavantage_key")
NEWS_API_KEY = os.environ.get("news_api_key")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
URL_ALPHAVANTAGE_API = "https://www.alphavantage.co/query"
URL_ALPHAVANTAGE_API_PARAMS = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}
#MAKE REQUEST AND STORE IN JSON FILE
    # with requests.get(URL_ALPHAVANTAGE_API, URL_ALPHAVANTAGE_API_PARAMS) as res:
    #     res.raise_for_status()
    #     daily_candles_data = res.json()
    #     with open("./Day036-erf/Stock_News/response_data.json", mode='w') as file:
    #         json.dump(daily_candles_data, file)

#READ FROM A JSON FILE TO PREVEN REPEATED API CALLS
with open("./Day036-erf/Stock_News/response_data.json", mode='r') as file:
    daily_candles_data = json.load(file)

#TODO: make some code to prevent raise exception for dates havent exist, instead replace that current_date with latest date db had.

def return_close_price(date):
    return float(daily_candles_data['Time Series (Daily)'][str(date)]['4. close'])


current_date = datetime.date(2025, 10, 17)
yesterday_date = current_date - datetime.timedelta(days=1)
yesterday_of_yesterday_date = yesterday_date - datetime.timedelta(days=1)

close_price_yesterday = return_close_price(yesterday_date)
close_price_2days_ago = return_close_price(yesterday_of_yesterday_date)

#CALCULATE PERCENTAGE OF DIFFRENCE
diff_percentage = 100 * (close_price_yesterday/close_price_2days_ago) - 100

if diff_percentage >= 5:
    print("Get News")

## STEP 2: Use https://newsapi.org
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

