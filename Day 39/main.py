#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_data()
pprint(sheet_data)