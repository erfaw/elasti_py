import subprocess as sp; sp.call('cls', shell=True)
import requests as rq
from bs4 import BeautifulSoup as bs
import json, pandas as pd
from pathlib import Path
_file_dir = Path(__file__).resolve().parent

class SongsData:
    def __init__(self):
        self.web_page:dict = None
        self.songs_db:pd.DataFrame = None

    def get_html_at(self, date:str) -> dict:
        """USE 'OFFICIALCHARTS' TO GET TOP 100 SONGS HTML PAGE ON THAT DATE FOR SCRAPING"""
        with rq.get(f"https://www.officialcharts.com/charts/singles-chart/{date}") as response:
            response.raise_for_status()
            parsed = bs(response.text, "html.parser")
            try:
                year_of_response = parsed.title.string.split()[6].split('/')[2]
                if len(parsed.title.string.split()[6].split('/')[1]) == 2:
                    month_of_response = parsed.title.string.split()[6].split('/')[1]
                elif len(parsed.title.string.split()[6].split('/')[1]) ==1:
                    month_of_response = f"0{parsed.title.string.split()[6].split('/')[1]}"
                if len(parsed.title.string.split()[6].split('/')[0]) == 2:
                    day_of_response = parsed.title.string.split()[6].split('/')[0]
                elif len(parsed.title.string.split()[6].split('/')[0]) ==1:
                    day_of_response = f"0{parsed.title.string.split()[6].split('/')[0]}"
            except IndexError:
                # TODO : make this block of code to a inner function with parameter i , to call it once with 6 and then with 4
                year_of_response = parsed.title.string.split()[4].split('/')[2]
                if len(parsed.title.string.split()[4].split('/')[1]) == 2:
                    month_of_response = parsed.title.string.split()[4].split('/')[1]
                elif len(parsed.title.string.split()[4].split('/')[1]) ==1:
                    month_of_response = f"0{parsed.title.string.split()[4].split('/')[1]}"
                if len(parsed.title.string.split()[4].split('/')[0]) == 2:
                    day_of_response = parsed.title.string.split()[4].split('/')[0]
                elif len(parsed.title.string.split()[4].split('/')[0]) ==1:
                    day_of_response = f"0{parsed.title.string.split()[4].split('/')[0]}"
            ## MAKE A DICT TO STORE DATA FOR SAVING Response FILE   
            web_page = {
                "input_date": date,
                "response_date": f"{year_of_response}{month_of_response}{day_of_response}",
                "html_response": response.text
            }
            return web_page

    def store_response(self) -> json:
        """SAVING FILE OF RESPONSE IN A JSON FILE"""
        path_to_save_response_json = Path('Day046-erf/output/responses/')
        path_to_save_response_json.mkdir(parents=True, exist_ok=True)
        with open(f"{path_to_save_response_json}/officialcharts_response_for_{self.web_page['response_date']}.json", mode='w') as file:
            json.dump(self.web_page, fp=file)
        print(f"response file successfully stored at <{path_to_save_response_json}>")

        # with open("./Day046-erf/officialcharts_response_for_20090705.json", mode='r') as web_page_data_file:
        #     web_page = json.load(web_page_data_file)

    def scrapte_to_songs_list(self):
        """SCRAPING 'self.web_page' TO GET A DATAFRAME OF TOP 100 SONGS AND STORE IT TO 'self.songs_db'"""
        self.web_page_parsed = bs(self.web_page['html_response'], "html.parser")
        ## SCRAPING TO LIST OF TOP 100 SONGS OF THAT DATE
        all_div = self.web_page_parsed.select(".chart-item-content")
        # MAKE DATAFRAME FOR STORE DATA
        self.songs_db = pd.DataFrame(columns=["Title", "Artist"])
        #LOOP THROUGH AND ADD TO DATAFRAME
        for track in all_div:
            # what we need? <track_name> <artist_name>
            track_name= track.select(".description p a")[0].select("span")[1].getText()
            artist_name= track.select(".description p a")[1].select("span")[0].getText()
            self.songs_db.loc[len(self.songs_db)] = {"Title": track_name, "Artist": artist_name}
        self.songs_db.index = pd.RangeIndex(start=1, stop= len(self.songs_db)+1, step=1)

    def store_to_excel(self, main_dir:Path):
        """STORE DATAFRAME which is in 'self.songs_db' INTO AN EXCEL FILE, ALONGSIDE MAIN FILE IN OUTPUT FOLDER"""
        path_to_save = main_dir/'output'
        path_to_save.mkdir(parents=True, exist_ok=True)
        self.songs_db.to_excel(f"{path_to_save}/{self.web_page["response_date"]}_top_100_songs.xlsx")
