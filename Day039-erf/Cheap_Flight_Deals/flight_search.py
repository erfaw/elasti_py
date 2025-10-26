import os
class FlightSearch:
    def __init__(self):
        """This class is responsible for talking to the Flight Search API."""
        self.URL_AMADEUS = "test.api.amadeus.com"
        self.API_KEY_AMADEUS = os.environ.get("API_KEY_AMADEUS")
        self.API_SECRET_AMADEUS = os.environ.get("API_SECRET_AMADEUS")
