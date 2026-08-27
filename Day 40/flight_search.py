import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"


class FlightSearch:

    def __init__(self):
        self.app_id = os.getenv("X_APP_ID")
        self.app_key = os.getenv("X_APP_KEY")
        self.url = "https://app.100daysofpython.dev/v1/flights/search"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self.app_key,
            "stops": "1"
        }

        if not is_direct:
            query["stops"] = "0"

        response = requests.get(url=API_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
