import requests
class ISS_Track:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_cor(self):
        "get now coordinate of ISS from api, then fill it to self.latitude and self.longitude"
        res_iss = requests.get("http://api.open-notify.org/iss-now.json")
        res_iss.raise_for_status()
        data = res_iss.json()
        self.latitude = float(data["iss_position"]["latitude"])
        self.longitude = float(data["iss_position"]["longitude"])   

    def is_it_close(self, lat, lng):
        """return True, if ISS coordinate was around our coordinate"""
        if lat-5 <= self.latitude <= lat+5 and lng-5 <= self.longitude <= lng+5: 
            return True
        else: 
            return False

        