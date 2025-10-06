import pandas as pd
class CardManager():
    def __init__(self):
        self.data = self.load_csv_file()

    def load_csv_file(self):
        db = pd.read_csv("./Day031-erf/data/1k_En_Per.csv").to_dict(orient='records')
        return db