from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
import os
from dotenv import load_dotenv

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.von_api_key = os.getenv("VON_API_KEY")
        self.api_secret = os.getenv("API_SECRET")

def send_message(self, notif_flights):
    for flight in notif_flights:
        client = Vonage(Auth(api_key=self.von_api_key, api_secret=self.api_secret))
        message = SmsMessage(
            to="19377015358",
            from_="16265491364",
            text=f"Low price alert! Only £{flight.price} to fly from {flight.origin_airport} to {flight.destination_airport}, "
                 f"on {flight.out_date} to {flight.return_date}.",
        )
        response: SmsResponse = client.sms.send(message)
        print(response)