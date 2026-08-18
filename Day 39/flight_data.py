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
    pass