import subprocess as sp; sp.call('cls', shell=True)
from data_manager import DataManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet = DataManager()
print(sheet.data)
