import os
import subprocess as sp; sp.call('cls', shell=True)
import datetime
from stock_price import StockPrice
from date_manager import DateManager

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ.get("alphavantage_key")
NEWS_API_KEY = os.environ.get("news_api_key")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock = StockPrice(STOCK, COMPANY_NAME, ALPHAVANTAGE_API_KEY)

#MAKE REQUEST AND STORE IN JSON FILE
# stock.daily_candles_data = stock.get_data()
# stock.store_to_json_file()
stock.daily_candles_data = stock.read_json_file()
stock.last_date_of_data = stock.last_date_exist()

date = DateManager()
date.today = date.current_date()
date.yesterday = date.yesterday_date()
date.before_yesterday = date.before_yesterday_date()

try:
    close_price_yesterday = stock.close_price(date.yesterday)
except KeyError: # catch exception for holidays, fill date.today with last data and date
    date.today = stock.last_date_of_data
    date.yesterday = date.yesterday_date()
    date.before_yesterday = date.before_yesterday_date()
    close_price_yesterday = stock.close_price(date.yesterday)
close_price_2days_ago = stock.close_price(date.before_yesterday)

#CALCULATE PERCENTAGE OF DIFFRENCE
change_percentage = stock.change_percentage(close_price_yesterday, close_price_2days_ago)

if change_percentage >= 5:
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

#TODO: make some code to prevent raise exception for dates havent exist, instead replace that current_date with latest date db had.