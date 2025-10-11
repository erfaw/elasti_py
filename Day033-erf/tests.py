import subprocess as sp; sp.call('cls', shell=True)
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

ISS_coordinate = (
    data['iss_position']['latitude'],
    data['iss_position']['longitude']
)

print(ISS_coordinate)