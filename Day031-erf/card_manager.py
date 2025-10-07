import pandas as pd
from random import choice
class CardManager():
    def __init__(self):
        self.data = self.load_csv_file()

    def load_csv_file(self):
        return pd.read_csv("./Day031-erf/data/1k_En_Per.csv").to_dict(orient='records')
         
    def random_choice(self):
        return choice(self.data)