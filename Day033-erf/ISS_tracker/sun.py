import requests
class SunSituation:
    def __init__(self):
        self.data = None
        self.sunrise_hour = None
        self.sunset_hour = None

    def get_situation(self, lat, lng):
        """request to api and get and fill self.data"""
        URL = 'https://api.sunrise-sunset.org/json'
        TIME_ZONE = 'Asia/Tehran'
        PARAMETERS = { # For arak
            'lat': lat,
            'lng': lng,
            'tzid': TIME_ZONE,
            'formatted': 0
        }  
        response = requests.get(url=URL, params=PARAMETERS)
        response.raise_for_status()
        self.data = response.json()
        

    def fill_hour_atts(self):
        """tap into self.data and catch Hour integer for sunrise and sunset and fill it to 'self.sunrise_hour' and 'self.sunset_hour'"""
        self.sunrise_hour = int(self.data['results']['sunrise'].split('T')[1].split(':')[0])
        self.sunset_hour = int(self.data['results']['sunset'].split('T')[1].split(':')[0])  
