import subprocess as sp; sp.call('cls', shell=True)
import requests
import pandas
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
data_to_pass = {
    "article_title": article_title,
    "article_link" : article_link,
    "article_upvote" : article_upvote
}
articles_data = pandas.DataFrame(data_to_pass,None, ["article_title", "article_link", "article_upvote"], None, True)
# articles_data.to_excel(excel_writer= "./Day045-erf/Beautiful_Soup/articles_data.xlsx",sheet_name='articles data', index=False)

highest_upvote_article = articles_data[articles_data["article_upvote"] == articles_data["article_upvote"].max()]

print(highest_upvote_article.get("article_link").item())