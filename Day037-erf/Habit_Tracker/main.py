import subprocess as sp; sp.call('cls', shell=True)
import requests, os

USERNAME = "erfawnhy"
TOKEN = os.environ.get("pixela_token")
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"
#Build a graph in api server
