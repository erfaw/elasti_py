import requests, json
import datetime
class StockPrice:
    def __init__(self, stock_name: str, company_name: str, api_key):
        """geting daily stock price data from 'alphavantage' site"""
        self.URL_ALPHAVANTAGE_API = "https://www.alphavantage.co/query"
        self.URL_ALPHAVANTAGE_API_PARAMS = {
            "function": 'TIME_SERIES_DAILY',
            "symbol": stock_name,
            "apikey": api_key,
        }
        self.stock_name = stock_name
        self.company_name = company_name
        self.daily_candles_data:json = None
        self.last_date_of_data = None

    def get_data(self) -> json:
        """request for data to api and return"""
        with requests.get(self.URL_ALPHAVANTAGE_API, self.URL_ALPHAVANTAGE_API_PARAMS) as res:
            res.raise_for_status()
            return res.json()

    def store_to_json_file(self):
        """store what is currently in 'self.daily_candles_data' to a file"""
        with open("./Day036-erf/Stock_News/stock_data.json", mode='w') as file:
            json.dump(self.daily_candles_data, file) 

    def read_json_file(self):
        """read data from resaponse_data.json and return """
        with open("./Day036-erf/Stock_News/stock_data.json", mode='r') as file:
            return json.load(file)

    def close_price(self,date):
        """return close price for that stock at a particular date catch with args"""
        return float(self.daily_candles_data['Time Series (Daily)'][str(date)]['4. close'])  

    def change_percentage(self, newer_date_price:float, earlier_date_price:float) -> float:
        """calculate and return change percentage between 2 date """
        return 100 * (newer_date_price/earlier_date_price) - 100
    
    def last_date_exist(self):
        """returns the last date of data that exist in 'self.daily_candles_data'"""
        string = next(iter(self.daily_candles_data["Time Series (Daily)"].keys()))
        list_1 = string.split('-')
        year = int(list_1[0])
        month = int(list_1[1])
        day = int(list_1[2])
        return datetime.date(year, month, day)
            