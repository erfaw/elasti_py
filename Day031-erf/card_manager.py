import pandas as pd
from random import choice
class CardManager():
    def __init__(self):
        self.data = self.load_csv_file()
        #mechanism to search through
        # for record in self.data:
        #     if record['English'] == 'of': 
        #         print('found')
        #     else:
        #         continue
        self.show_card = None

    def load_csv_file(self):
        try:
            f=open('./Day031-erf/data/words_to_learn.csv', mode='r')
        except FileNotFoundError:
            raw_data = pd.read_csv("./Day031-erf/data/1k_En_Per.csv")
            raw_data.to_csv('./Day031-erf/data/words_to_learn.csv')
        else:
            f.close()
        finally:
            return pd.read_csv("./Day031-erf/data/words_to_learn.csv").to_dict(orient='records')
         
    def random_choice(self):
        return choice(self.data)
    
    def delete_record(self, english_word):
        # remove english_word from self.data
        if self.show_card:
            self.data.remove(english_word)
            
            # must delete english_word:str record from words_to_learn.csv
            raw_to_save = pd.DataFrame(self.data)
            raw_to_save.to_csv('./Day031-erf/data/words_to_learn.csv')
        else: 
            pass
