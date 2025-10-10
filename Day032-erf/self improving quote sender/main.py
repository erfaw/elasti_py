import subprocess as sp; sp.call('cls', shell=True)
import smtplib
import datetime as dt
from random import choice
my_email = 'erfawn.h@gmail.com'
password = '' 
now = dt.datetime.now()
day_of_week = now.weekday()

#DONE: obtain list of quotes
with open('./Day032-erf/Birthday_Wisher/quotes.txt', mode='r') as file:
    data = file.readlines()
#DONE: pick a random quote
random_quote = choice(data)
#DONE: mail random quote if day of week was 4 to yourself
if day_of_week == 4:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Self-improving Quote\n\n{random_quote}")
else: pass
