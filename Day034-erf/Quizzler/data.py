import requests
import subprocess as sp; sp.call('cls', shell=True)
# build a request to api and implement to 'question_data' and then; comment out below
API = 'https://opentdb.com/api.php'
#TODO: add some sort of functionality to ui and data to ask the user with GUI which category he like to play
PARAMETERS = {
    'type': 'boolean',
    'amount': 10
    #TODO: add a field here name 'category' and fill it with user choice of category he/she like to play with
}
res = requests.get(API, PARAMETERS)
res.raise_for_status()
question_data = res.json()["results"]
