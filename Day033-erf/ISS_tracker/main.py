import subprocess as sp; sp.call('cls', shell=True)
import requests
import threading
from datetime import datetime
from iss_track import ISS_Track
from sun import SunSituation
from mail_sender import GmailSender
ARAK_LATITUDE = 34.092229
ARAK_LONGITUDE = 49.721958
mail = GmailSender()
iss = ISS_Track()
sun = SunSituation()

def is_dark_sky():
    """return True if sky is dark and we could see a space station"""
    if sun.sunset_hour < current_hour < sun.sunrise_hour :
        return True
    else: 
        return False

def main():
    global current_hour
    sp.call('cls', shell=True)
    iss.get_cor()
    sun.get_situation(lat= ARAK_LATITUDE, lng= ARAK_LONGITUDE)
    sun.fill_hour_atts()
    current_hour = datetime.now().hour

    print(f"sunrise hour is ===> {sun.sunrise_hour}")
    print(f"sunset hour is ===> {sun.sunset_hour}")
    print(f"current hour is ===> {current_hour}")
    print(f"ISS now coordinate is (lat,lng) ===> {iss.latitude} , {iss.longitude}")
    print(f"is ISS close to me? ==> {iss.is_it_close(lat= ARAK_LATITUDE, lng= ARAK_LONGITUDE)}")
    print(f"is it dark enough to see space station? ==> {is_dark_sky()}")

    if iss.is_it_close(lat= ARAK_LATITUDE, lng= ARAK_LONGITUDE) and is_dark_sky():
        mail.send(
            sender_email= "erfawn.h@gmail.com",
            sender_app_password= "givl ankx ezxx dxih",
            recipient_email= "erfawn.h@gmail.com",
            subject= "LOOK UPPPP!!!!",
            message_to_send= "ISS is just right up of your head, go and see it :) !"
        )
    else: 
        print('NOT HERE')
        # mail.send(
        # sender_email= "erfawn.h@gmail.com",
        # sender_app_password= "givl ankx ezxx dxih",
        # recipient_email= "erfawn.h@gmail.com",
        # subject= "DONE LOOK!",
        # message_to_send= "after many circumstances you cant see it right now!"
        # )
    threading.Timer(60, main).start()

main()

# ---- TODOS ---- #
#DONE: catch the data from api related to sunrise and sunset of arak
#DONE: parse data to 24h formated
#DONE: catch now.hour 
#DONE: added ISS_coordinate codes here, and print it
#DONE: OOP all of ISS and Sun
#DONE: catch the moment which ISS is close to my current location (-5 +5)
#DONE: check if is it currently dark or not (it must be after sunset and before sunrise)
#DONE: if was: send an email to tell me look up
#TODO: RUN the code every