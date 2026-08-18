#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=182)
tomorrow = tomorrow.strftime("%Y-%m-%d")
six_months_from_now = six_months_from_now.strftime("%Y-%m-%d")


flight_search = FlightSearch()
flight_data = flight_search.check_flights(
                            from_airport_code="LHR",
                            to_airport_code=sheet_data[0]["iataCode"],
                            from_time=tomorrow,
                            to_time=six_months_from_now,
)
pprint(flight_data)

