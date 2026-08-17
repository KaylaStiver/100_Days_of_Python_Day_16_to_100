import requests
import datetime
import os

url = "https://app.100daysofpython.dev"
post = "/v1/nutrition/natural/exercise"

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("APP_KEY"),
}

parameters = {
    "query": input("What exercise did you do today?: "),
}

response = requests.post(url+post, json=parameters, headers=headers)
exercise_data = response.json()

sheety_url = "https://api.sheety.co/1ddb4da1d13c0612d3ad519bb2a6712f/workoutTracking/workouts"
today = datetime.datetime.now()
hour = today.strftime("%H:%M:%S")
today = today.strftime("%d/%m/%Y")

sheety_user = os.getenv("USERNAME")
sheety_pass = os.getenv("PASSWORD")

body = {
    "workout": {
        "date": today,
        "time": hour,
        "exercise": exercise_data["exercises"][0]["name"].title(),
        "duration": exercise_data["exercises"][0]["duration_min"],
        "calories": exercise_data["exercises"][0]["nf_calories"],
    },
}

sheety_response = requests.post(sheety_url, json=body, auth=(sheety_user, sheety_pass))
sheet_data = sheety_response.json()
print(sheet_data)
