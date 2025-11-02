import subprocess as sp; sp.call('cls', shell=True)
from bs4 import BeautifulSoup as bs
import requests as rq
import lxml
import pandas as pd
## AS ALWAYS, WE HAVE 'GEO-BLOCKING' ON EMIREONLINE,
    # with rq.get("https://www.empireonline.com/movies/features/best-movies-2/") as rs:

##INSTEAD, WE USE this
with rq.get("https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time") as rs: #request to site to get html and parse it to 'web_page'
    rs.raise_for_status()
    web_page = bs(rs.text, "html.parser") 

all_articles = web_page.select(selector=".ResultsPage__ResultGrid-sc-of10co-0 article") #selecting all articles which have movie detials
movies_db = pd.DataFrame( # make dataFrame but empty
    columns= ["title", "year_country", "director"],
    index= range(1) #for starting wiht 1
)
for article in all_articles: # loop through and get the details, then store it in DataFrame
    title = article.select_one("h1").getText()
    year_country = article.select(".MbGOi")[0].getText()
    director = " ".join(article.select(".MbGOi")[1].getText().split()[2:])
    movies_db.loc[len(movies_db)] = {'title': title, 'year_country': year_country, 'director': director}

movies_db.sort_index(ascending=False, inplace=True) # sort Descending to seem like actual site
movies_db.drop(index=0, axis=0, inplace=True) #drop index 0 which is empty and exist just for indexing start at 1

movies_db.to_excel("./Day045-erf/Beautiful_Soup/Empire_100_top_movie_scraping/top_movies_list.xlsx") # at the end: store result to a excel file
