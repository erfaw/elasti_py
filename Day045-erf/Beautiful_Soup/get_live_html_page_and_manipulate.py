import subprocess as sp; sp.call('cls', shell=True)
import requests
from bs4 import BeautifulSoup
with requests.get(url="https://news.ycombinator.com/") as response:
    response.raise_for_status()
    web_page = BeautifulSoup(response.text, 'html.parser')

##GET TITLE OF FIRST ARTICLE ON HACKERNEWS
first_article = web_page.select_one(
    selector=".titleline a"
)
first_article_title = first_article.getText()
first_article_link:str = first_article.get('href')
first_article_upvote:str = web_page.select_one(selector=".score").getText()
first_article_upvote_num:int = int(first_article_upvote[:first_article_upvote.index('p')])

print(
    f"first article title is:\n\t{first_article_title}\nfirst article upvote str is:\n\t{first_article_upvote} and {first_article_upvote_num} as an integer number\nfirst article link is: \n\t{first_article_link}"
)