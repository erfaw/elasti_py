import subprocess as sp; sp.call('cls', shell=True)
from bs4 import BeautifulSoup
with open("./Day045-erf/Beautiful_Soup/website.html", mode='r') as web_page:
    contents = web_page.read()

soup = BeautifulSoup(contents, "html.parser")
