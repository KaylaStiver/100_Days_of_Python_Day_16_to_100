from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
import os
from dotenv import load_dotenv
import smtplib

class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.von_api_key = os.getenv("VON_API_KEY")
        self.api_secret = os.getenv("API_SECRET")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")

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

    def send_emails(self, email_list, email_body):
        for email in email_list:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.password)
                connection.sendmail(from_addr=self.email, to_addrs=email,
                                    msg=f"Subject:New Low Price Flight Alert!\n\n{email_body}")