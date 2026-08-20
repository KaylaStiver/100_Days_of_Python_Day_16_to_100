from datetime import datetime, timedelta

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.origin_airport = "LHR"
        self.destination_airport = ""
        self.out_date = datetime.now() + timedelta(days=1)
        self.return_date = self.out_date + timedelta(days=182)

def find_cheapest_flight(data, return_date):
    flights = data.get("best_flights", []) + data.get("other_flights", [])
    cheapest_flight = FlightData()
    for flight in flights:
        if flight.get("price") is None:
            continue
        if cheapest_flight.price == 0:
            cheapest_flight.price = flight.get("price")
            cheapest_flight.origin_airport = flight["flights"][0]["departure_airport"]["id"]
            cheapest_flight.destination_airport = flight["flights"][-1]["arrival_airport"]["id"]
            cheapest_flight.out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight.return_date = return_date
        elif cheapest_flight.price > flight.get("price"):
            cheapest_flight.price = flight.get("price")
            cheapest_flight.origin_airport = flight["flights"][0]["departure_airport"]["id"]
            cheapest_flight.destination_airport = flight["flights"][-1]["arrival_airport"]["id"]
            cheapest_flight.out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
    return cheapest_flight


