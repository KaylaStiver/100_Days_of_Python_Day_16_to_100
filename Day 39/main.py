#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_data()
print(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=182)

flight_search = FlightSearch()
# flight_search.check_flights(sheet_data[[]])

