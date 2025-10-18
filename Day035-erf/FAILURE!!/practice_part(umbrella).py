import subprocess as sp; sp.call('cls', shell=True)
import requests
import json
from datetime import *

api_key = "a37af2c856efa25f90ee8e7546fcaeef"
URL_5DAY_3HOUR_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"
URL_CURRENT_DATA = "https://api.openweathermap.org/data/2.5/weather"
ARAK_LATITUDE = 34.092229
ARAK_LONGITUDE = 49.721958
e_lat = 48.380894
e_lon = -89.247681
PARAMETERS = {
    'lat': e_lat,
    'lon': e_lon,
    'appid': api_key,
    'cnt': 4,
}
# REQUEST PART AND STORE FOR MORE GRINDING
response = requests.get(URL_5DAY_3HOUR_FORECAST,PARAMETERS)
response.raise_for_status()
    # # print(response.json())
data = response.json()
    # with open ('./Day035-erf/data.json', mode='w') as file:
    #     # file.write(data)
    #     json.dump(data,file)

# READING STORED FILE 
    # with open('./Day035-erf/data.json', mode='r') as file:
    #     data = json.load(file)
    
will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella!')
else: print('you are not going to wet to day :) ')