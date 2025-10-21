import os
import subprocess as sp; sp.call('cls', shell=True)
from stock_price import StockPrice
from date_manager import DateManager
from news import News
from mail_sender import GmailSender

##CONSTS
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.environ.get("alphavantage_key")
NEWS_API_KEY = os.environ.get("news_api_key")
GMAIL_API_KEY = os.environ.get("gmail_key")

##OBJECTS
gmail = GmailSender()
date = DateManager()
stock = StockPrice(STOCK, COMPANY_NAME, ALPHAVANTAGE_API_KEY)
news = News(
    api_key= NEWS_API_KEY,
    search_key= COMPANY_NAME,
    from_date= stock.all_dates[2]
    )

##STORE DATES WE NEED
date.yesterday = stock.all_dates[0]
date.before_yesterday = stock.all_dates[1]

##CALCULATE AND STORE CLOSE PRICES and CHANGE PRICE PERCENTAGE
stock.close_price_yesterday = stock.close_price(date.yesterday)
stock.close_price_2days_ago = stock.close_price(date.before_yesterday)
stock.change_price_percentage = stock.change_percentage(stock.close_price_yesterday, stock.close_price_2days_ago)

if stock.change_price_percentage >= 1:
    news.data_result = news.get_data()
    news.store_to_json_file()
    up_down_char = None
    if stock.change_price_percentage > 0:
        up_down_char = '🟢🔺'
    elif stock.change_price_percentage < 0:
        up_down_char = '🔴🔻'
    else: pass
    #LOOP THROUGH AND SEND gmail
    for article in news.data_result["articles"]:
        gmail.send(
            sender_email='erfawn.h@gmail.com',
            sender_app_password= GMAIL_API_KEY,
            recipient_email='erfawn.h@gmail.com',
            subject=f"{STOCK}: {stock.change_price_percentage:.2f}%",
            message_to_send=f"Headline: {article["title"]}\nBrief: {article["description"]}\nURL to check: {article["url"]}".replace('\u2018', '').replace('\u2014', '-').replace('\u2019','').replace('\u2013','')
        )

#TODO: make some code to prevent raise exception for dates havent exist, instead replace that current_date with latest date db had.