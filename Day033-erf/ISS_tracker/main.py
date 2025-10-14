import subprocess as sp; sp.call('cls', shell=True)
import requests
from datetime import datetime
from iss_track import ISS_Track
from sun import SunSituation
ARAK_LATITUDE = 34.092229
ARAK_LONGITUDE = 49.721958

iss = ISS_Track()
iss.get_cor()

sun = SunSituation()
sun.get_situation(lat= ARAK_LATITUDE, lng= ARAK_LONGITUDE)
sun.fill_hour_atts()

current_hour = datetime.now().hour

print(f"sunrise hour is ===> {sun.sunrise_hour}")
print(f"sunset hour is ===> {sun.sunset_hour}")
print(f"current hour is ===> {current_hour}")
print(f"ISS now coordinate is (lat,lng) ===> {iss.latitude} , {iss.longitude}")



# ---- TODOS ---- #
#DONE: catch the data from api related to sunrise and sunset of arak
#DONE: parse data to 24h formated
#DONE: catch now.hour 
#DONE: added ISS_coordinate codes here, and print it
#DONE: OOP all of ISS and Sun

#TODO: catch the moment which ISS is close to my current location (-5 +5)
#TODO: check if is it currently dark or not (it must be after sunset and before sunrise)
#TODO: if was: send an email to tell me look up
#TODO: RUN the code every 60s