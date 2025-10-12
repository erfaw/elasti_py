import requests
class ISS_Track:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_cor(self):
        "get now coordinate of ISS from api, then return it as a tuple -> (lat,lng)"
        res_iss = requests.get("http://api.open-notify.org/iss-now.json")
        res_iss.raise_for_status()
        data = res_iss.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])   
        return (iss_latitude, iss_longitude)