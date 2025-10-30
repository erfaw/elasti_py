# # requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# import os, requests
# class FlightSearch:
#     def __init__(self):
#         """This class is responsible for talking to the Flight Search API."""
#         self.URL_AMADEUS = "https://test.api.amadeus.com"
#         self.API_KEY_AMADEUS = os.environ.get("API_KEY_AMADEUS")
#         self.API_SECRET_AMADEUS = os.environ.get("API_SECRET_AMADEUS")
#         self.ACCESS_TOKEN_AMADEUS = os.environ.get("ACCESS_TOKEN_AMADEUS")
#         self.URL_FLIGHT_DESTINATION = f"{self.URL_AMADEUS}/v1/shopping/flight-destinations"

#     def get_request(self):
#         headers = {
#             "Authorization": f"Bearer {self.ACCESS_TOKEN_AMADEUS}"
#         }
#         params = {
#             "origin": "MAD",
#             "maxPrice": 200
#         }
#         with requests.get(
#             url= self.URL_FLIGHT_DESTINATION,
#             params= params,
#             headers=headers
#         ) as res:
#             print(res.text)
        

#     def get_access_token(self):
#         """NOTICE: first try to catch it from EV: make POST request to get access token from site, NOTICE: NOT WORKS WITH IRANS IP"""
#         headers = {
#             "Content-Type": "application/x-www-form-urlencoded"
#         }
#         body_request = {
#             "grant_type": "client_credentials",
#             "client_id": self.API_KEY_AMADEUS,
#             "client_secret": self.API_SECRET_AMADEUS
#         }
#         with requests.post( #NOTICE: THIS NOT WORK WITH IRANS IP
#             url= f"{self.URL_AMADEUS}/v1/security/oauth2/token",
#             data= body_request,
#             headers= headers
#         ) as res:
#             res.raise_for_status()
#             return res.json()
#             # return res
        
