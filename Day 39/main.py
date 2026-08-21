#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager, send_message

#Obtain data from Google Sheet
data_manager = DataManager()
sheet_data = data_manager.get_data()

#Format tomorrow's date and date six months from now
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=182)
tomorrow = tomorrow.strftime("%Y-%m-%d")
six_months_from_now = six_months_from_now.strftime("%Y-%m-%d")

#Search for flights during this time period
flight_search = FlightSearch()
notif_flights = []
for i in range(0,3):
    flight_data = flight_search.check_flights(
                                from_airport_code="LHR",
                                to_airport_code=sheet_data[i]["iataCode"],
                                from_time=tomorrow,
                                to_time=six_months_from_now,
    )
#For each city in the Google Sheet, find the cheapest flight
    flight = find_cheapest_flight(flight_data, six_months_from_now)
#If the cheapest flight available is lower than the Google Sheet price, save to a list
    if flight.price < sheet_data[i]["price"]:
        notif_flights.append(flight)

#Send text message to notify of the cheapest available flights for each city
notif_manager = NotificationManager()
send_message(notif_manager, notif_flights)

