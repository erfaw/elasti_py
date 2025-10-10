##################### Extra Hard Starting Project ######################
import subprocess as sp; sp.call('cls', shell=True)
import pandas as pd
import datetime as dt
#DONE: Update the birthdays.csv

#DONE: Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("./Day032-erf/birthday-wisher-extrahard/birthdays.csv")
# print(data)
now = dt.datetime.now()

birthday_matched = data[(data.month == now.month) & (data.day == now.day)]

print(birthday_matched)


#TODO: If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

#TODO: Send the letter generated in step 3 to that person's email address.




