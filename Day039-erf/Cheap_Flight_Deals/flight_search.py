import os, requests
class FlightSearch:
    def __init__(self):
        """This class is responsible for talking to the Flight Search API."""
        self.URL_AMADEUS = "https://test.api.amadeus.com"
        self.API_KEY_AMADEUS = os.environ.get("API_KEY_AMADEUS")
        self.API_SECRET_AMADEUS = os.environ.get("API_SECRET_AMADEUS")
        self.ACCESS_TOKEN_AMADEUS = os.environ.get("ACCESS_TOKEN_AMADEUS")

    def get_access_token(self):
        """NOTICE: first try to catch it from EV: make POST request to get access token from site"""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body_request = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY_AMADEUS,
            "client_secret": self.API_SECRET_AMADEUS
        }
        with requests.post(
            url= f"{self.URL_AMADEUS}/v1/security/oauth2/token",
            data= body_request,
            headers= headers
        ) as res:
            res.raise_for_status()
            return res.json()
            # return res
        
