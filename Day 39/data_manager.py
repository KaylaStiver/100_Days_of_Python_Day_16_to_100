import requests
from dotenv import load_dotenv
import os


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.sheety_url = os.getenv("SHEETY_URL")
        self.sheety_user = os.getenv("SHEETY_USER")
        self.sheety_pass = os.getenv("SHEETY_PASS")

    def get_data(self):
        sheety_response = requests.get(self.sheety_url, auth=(self.sheety_user, self.sheety_pass))
        sheet_data = sheety_response.json()
        sheet_data = sheet_data["sheet1"]
        return sheet_data