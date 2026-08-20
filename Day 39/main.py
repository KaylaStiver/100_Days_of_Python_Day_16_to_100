#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight

data_manager = DataManager()
sheet_data = data_manager.get_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=182)
tomorrow = tomorrow.strftime("%Y-%m-%d")
six_months_from_now = six_months_from_now.strftime("%Y-%m-%d")


flight_search = FlightSearch()
for i in range(0,3):
    flight_data = flight_search.check_flights(
                                from_airport_code="LHR",
                                to_airport_code=sheet_data[i]["iataCode"],
                                from_time=tomorrow,
                                to_time=six_months_from_now,
    )
    flight = find_cheapest_flight(flight_data, six_months_from_now)
    pprint(f"{flight.destination_airport}: GBP {flight.price}")


