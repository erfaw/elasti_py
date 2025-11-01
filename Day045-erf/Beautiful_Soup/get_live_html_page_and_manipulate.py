import subprocess as sp; sp.call('cls', shell=True)
import requests
from bs4 import BeautifulSoup
with requests.get(url="https://news.ycombinator.com/") as response:
    response.raise_for_status()
    web_page = BeautifulSoup(response.text, 'html.parser')

print(web_page.title.string)