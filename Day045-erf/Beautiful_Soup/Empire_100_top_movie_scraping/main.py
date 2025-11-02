import subprocess as sp; sp.call('cls', shell=True)
from bs4 import BeautifulSoup as bs
import requests as rq
import lxml
## AS ALWAYS, WE HAVE 'GEO-BLOCKING' ON EMIREONLINE,
    # with rq.get("https://www.empireonline.com/movies/features/best-movies-2/") as rs:

##INSTEAD, WE USE this
with rq.get("https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time") as rs:
    rs.raise_for_status()
    web_page = bs(rs.text, "html.parser")

# all_articles = web_page.select(selector=".ResultsPage__ResultGrid-sc-of10co-0 article")

##catch first title 
first_title = web_page.select_one(".dzyNha a h1").getText()
print(first_title)


# print(all_articles)
# print(len(all_articles))
