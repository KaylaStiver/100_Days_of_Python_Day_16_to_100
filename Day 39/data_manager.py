import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = "https://api.sheety.co/1ddb4da1d13c0612d3ad519bb2a6712f/flightData/sheet1"
        self.sheety_user = "spicyNby8&K$44"
        self.sheety_pass = "ioyyiaueisharp"

    def get_data(self):
        sheety_response = requests.post(self.sheety_url, auth=(self.sheety_user, self.sheety_pass))
        sheet_data = sheety_response.json()
        print(sheet_data)