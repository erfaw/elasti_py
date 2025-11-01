import subprocess as sp; sp.call('cls', shell=True)
import requests
from bs4 import BeautifulSoup
with requests.get(url="https://news.ycombinator.com/") as response:
    response.raise_for_status()
    web_page = BeautifulSoup(response.text, 'html.parser')

all_tr = web_page.select(
    selector="#bigbox table tr"
)[:-2] #except last 2 , they wasn't article
articles = []
#slice 3 by 3 
for i in range(0, len(all_tr), 3):
    articles.append(all_tr[i:i+3])

article_title = []
article_link = []
article_upvote = []
for article in articles:
    article_title.append(article[0].find(class_="titleline").getText())
    article_link.append(article[0].select(selector=".titleline a")[0].get('href'))
    article_upvote.append(
        int(article[1].select(selector=".score")[0].getText().split()[0])
    )
print(f"{len(article_title)}\n{len(article_link)}\n{len(article_upvote)}")
    
# first_article_title = first_article.getText()
# first_article_link:str = first_article.get('href')
# first_article_upvote:str = web_page.select_one(selector=".score").getText()
# first_article_upvote_num:int = int(first_article_upvote[:first_article_upvote.index('p')])

# print(
#     f"first article title is:\n\t{first_article_title}\nfirst article upvote str is:\n\t{first_article_upvote} and {first_article_upvote_num} as an integer number\nfirst article link is: \n\t{first_article_link}"
# )