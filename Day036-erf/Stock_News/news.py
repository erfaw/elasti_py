import requests, json, datetime as dt
class News:
    def __init__(self, api_key, search_key, from_date='', to_date='', num_article=3):
        """get news about 'search_key'\n"""
        self.api_key = api_key
        # self.NEWS_URL = "https://newsapi.org/v2/top-headlines"
        self.NEWS_URL = "https://newsapi.org/v2/everything"
        self.NEWS_URL_PARAMS = {
            'apiKey': self.api_key,
            'q': search_key,
            'language': 'en',
            'from': from_date,
            'to': to_date,
            'pageSize': num_article
        }
        self.data_result = None

    def get_data(self):
        """request to api and catch data then return"""
        with requests.get(self.NEWS_URL, self.NEWS_URL_PARAMS) as res:
            res.raise_for_status()
            return res.json()
        
    def store_to_json_file(self):
        """store what is currently in 'self.data_result' to a json file"""
        with open("./Day036-erf/Stock_News/json/news_data.json", mode='w') as file:
            json.dump(self.data_result, file)

    def read_json_file(self):
        """read data from news_data.json and return """
        with open("./Day036-erf/Stock_News/json/news_data.json", mode='r') as file:
            return json.load(file)