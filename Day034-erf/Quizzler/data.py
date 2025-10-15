import requests
import subprocess as sp; sp.call('cls', shell=True)
# build a request to api and implement to 'question_data' and then; comment out below
API = 'https://opentdb.com/api.php'
PARAMETERS = {
    'type': 'boolean',
    'amount': 10
}
res = requests.get(API, PARAMETERS)
res.raise_for_status()
question_data = res.json()["results"]
