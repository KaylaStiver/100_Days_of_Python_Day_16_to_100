import os
import requests
from dotenv import load_dotenv


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        load_dotenv()
        self.app_id = os.getenv("X_APP_ID")
        self.app_key = os.getenv("X_APP_KEY")
        self.url = "https://app.100daysofpython.dev/v1/flights/search"

    def check_flights(self, from_airport_code, to_airport_code, from_time, to_time):
        parameters = {
            "engine": "google_flights",
            "departure_id": from_airport_code,
            "arrival_id": to_airport_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.app_key,
        }

        response = requests.get(self.url, params=parameters)
        return response.json()
