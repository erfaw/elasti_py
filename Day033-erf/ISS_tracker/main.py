import subprocess as sp; sp.call('cls', shell=True)
import requests
from datetime import datetime
# catch data from ISS coordinate from api
res_iss = requests.get("http://api.open-notify.org/iss-now.json")
res_iss.raise_for_status()
data = res_iss.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

URL = 'https://api.sunrise-sunset.org/json'
ARAK_LATITUDE = 34.092229
ARAK_LONGITUDE = 49.721958
TIME_ZONE = 'Asia/Tehran'
PARAMETERS = { # For arak
    'lat': ARAK_LATITUDE,
    'lng': ARAK_LONGITUDE,
    'tzid': TIME_ZONE,
    'formatted': 0
}

response = requests.get(url=URL, params=PARAMETERS)
response.raise_for_status()
data = response.json()
# parse to catch 24h formated hour
sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
print(f"sunrise hour is ===> {sunrise_hour}")
print(f"sunset hour is ===> {sunset_hour}")

current_hour = datetime.now().hour
print(f"current hour is ===> {current_hour}")
print(f"ISS now coordinate is (lat,lng) ===> {ISS_coordinate}")


# ---- TODOS ---- #
#DONE: catch the data from api related to sunrise and sunset of arak
#DONE: parse data to 24h formated
#DONE: catch now.hour 
#DONE: added ISS_coordinate codes here, and print it