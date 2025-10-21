import os
import subprocess as sp; sp.call('cls', shell=True)
import datetime
from stock_price import StockPrice
from date_manager import DateManager
from news import News
from mail_sender import GmailSender

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ.get("alphavantage_key")
NEWS_API_KEY = os.environ.get("news_api_key")
GMAIL_API_KEY = os.environ.get("gmail_key")

stock = StockPrice(STOCK, COMPANY_NAME, ALPHAVANTAGE_API_KEY)
gmail = GmailSender()
date = DateManager()

#MAKE REQUEST AND STORE IN JSON FILE
stock.daily_candles_data = stock.get_data()
stock.store_to_json_file()
# stock.daily_candles_data = stock.read_json_file()
stock.last_date_of_data = stock.last_date_exist()
stock.all_dates = stock.all_of_dates()

date.today = date.current_date()
date.yesterday = stock.all_dates[0]
date.before_yesterday = stock.all_dates[1]

close_price_yesterday = stock.close_price(date.yesterday)
close_price_2days_ago = stock.close_price(date.before_yesterday)

#CALCULATE PERCENTAGE OF DIFFRENCE
change_percentage = stock.change_percentage(close_price_yesterday, close_price_2days_ago)

if change_percentage >= 1:
    news = News(
        api_key= NEWS_API_KEY,
        search_key= COMPANY_NAME,
        from_date= stock.all_dates[2]
        )
    news.data_result = news.get_data()
    news.store_to_json_file()
    # news.data_result = news.read_json_file()

    up_down_char = None
    if change_percentage > 0:
        up_down_char = '🟢🔺'
    elif change_percentage < 0:
        up_down_char = '🔴🔻'
    else: pass

    #LOOP THROUGH AND SEND 
    for article in news.data_result["articles"]:
        gmail.send(
            sender_email='erfawn.h@gmail.com',
            sender_app_password= GMAIL_API_KEY,
            recipient_email='erfawn.h@gmail.com',
            subject=f"{STOCK}: {change_percentage:.2f}%",
            message_to_send=f"Headline: {article["title"]}\nBrief: {article["description"]}\nURL to check: {article["url"]}".replace('\u2018', '').replace('\u2014', '-').replace('\u2019','').replace('\u2013','')
        )

#TODO: make some code to prevent raise exception for dates havent exist, instead replace that current_date with latest date db had.