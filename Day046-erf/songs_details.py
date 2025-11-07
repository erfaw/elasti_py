import subprocess as sp; sp.call('cls', shell=True)
import requests as rq
from bs4 import BeautifulSoup as bs
import json, pandas as pd

## ASK USER IN WHICH TIME
        # time_to_check = input("Which year do you want to travel to? (Type the date in this format YYYYMMDD)\n\t")

## USE 'OFFICIALCHARTS' INSTEAD OF 'BILLBOARD' (BEACUASE GEO-BLOCKING) TO GET TOP 100 SONGS ON THAT DATE
        # with rq.get(f"https://www.officialcharts.com/charts/singles-chart/{time_to_check}") as response:
        #     response.raise_for_status()
        #     parsed = bs(response.text, "html.parser")
        #     year_of_response = parsed.title.string.split()[4].split('/')[2]
        #     if len(parsed.title.string.split()[4].split('/')[1]) == 2:
        #         month_of_response = parsed.title.string.split()[4].split('/')[1]
        #     elif len(parsed.title.string.split()[4].split('/')[1]) ==1:
        #         month_of_response = f"0{parsed.title.string.split()[4].split('/')[1]}"
        #     if len(parsed.title.string.split()[4].split('/')[0]) == 2:
        #         day_of_response = parsed.title.string.split()[4].split('/')[0]
        #     elif len(parsed.title.string.split()[4].split('/')[0]) ==1:
        #         day_of_response = f"0{parsed.title.string.split()[4].split('/')[0]}"
        #     ## MAKE A DICT TO STORE DATA FOR SAVING FILE   
        #     web_page = {
        #         "input_date": time_to_check,
        #         "response_date": f"{year_of_response}{month_of_response}{day_of_response}",
        #         "html_response": response.text
        #     }
        #     ## OPEN AND SAVING FILE
        #     with open(f"./Day046-erf/officialcharts_response_for_{web_page['response_date']}.json", mode='w') as file:
        #         json.dump(web_page, fp=file)

with open("./Day046-erf/officialcharts_response_for_20090705.json", mode='r') as web_page_data_file:
    web_page = json.load(web_page_data_file)

web_page_parsed = bs(web_page['html_response'], "html.parser")

## SCRAPING TO LIST OF TOP 100 SONGS OF THAT DATE
all_div = web_page_parsed.select(".chart-item-content")
# MAKE DATAFRAME FOR STORE DATA
songs_db = pd.DataFrame(columns=["Title", "Artist"])
#LOOP THROUGH AND ADD TO DATAFRAME
for track in all_div:
    # what we need? <track_name> <artist_name> <album_name> <release_date> etc
    track_name= track.select(".description p a")[0].select("span")[1].getText()
    artist_name= track.select(".description p a")[1].select("span")[0].getText()
    songs_db.loc[len(songs_db)] = {"Title": track_name, "Artist": artist_name}
songs_db.index = pd.RangeIndex(start=1, stop= len(songs_db)+1, step=1)
#STORE DATAFRAME IN OUTPUT FOLDER
try:
    songs_db.to_excel(f"./Day046-erf/output/top_100_songs_at_{web_page["response_date"]}.xlsx")
except OSError: 
    sp.call('mkdir .\Day046-erf\output', shell=True)
    songs_db.to_excel(f"./Day046-erf/output/top_100_songs_at_{web_page["response_date"]}.xlsx")