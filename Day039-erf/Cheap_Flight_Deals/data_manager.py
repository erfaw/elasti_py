import subprocess as sp; sp.call('cls', shell=True)
import requests, os
class DataManager:
    def __init__(self):
        """This class is responsible for talking to the Google Sheet."""
        self.SHEETY:dict = {
            "ENDPOINT": "https://api.sheety.co/54bdfdd6059a5dd8664f1a638dbf3770",
            "PROJECT": "flightDeals",
            "SHEET": "prices",
            "HEADERS": {
                "Authorization": os.environ.get("sheety_api_token")
            }
        }
        self.data:dict = self.get_data()

    def get_data(self) -> dict:
        """get data from sheet file and return (dict)"""
        with requests.get(
        url= f"{self.SHEETY["ENDPOINT"]}/{self.SHEETY["PROJECT"]}/{self.SHEETY["SHEET"]}",
        headers= self.SHEETY["HEADERS"]
            ) as response:
                return response.json()
                