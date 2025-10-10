##################### Extra Hard Starting Project ######################
import subprocess as sp; sp.call('cls', shell=True)
import pandas as pd
import datetime as dt
from random import randint
from mail_sender import GmailSender
#DONE: Update the birthdays.csv

#DONE: Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("./Day032-erf/birthday-wisher-extrahard/birthdays.csv")
now = dt.datetime.now()
birthday_matched = data[(data.month == now.month) & (data.day == now.day)]

#DONE: If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# pick a random letter
with open(f'./Day032-erf/birthday-wisher-extrahard/letter_templates/letter_{randint(1,3)}.txt') as file:
    letter_str = file.read()

#replace [NAME]
letter_str = letter_str.replace('[NAME]', birthday_matched['name'].to_string(index=False).capitalize())

#TODO: Send the letter generated in step 3 to that person's email address.
mail = GmailSender()
mail.send(
    'erfawn.h@gmail.com',
    'givl ankx ezxx dxih',
    birthday_matched.email.to_string(index= False),
    'Happy Birthday!!!',
    letter_str
)



