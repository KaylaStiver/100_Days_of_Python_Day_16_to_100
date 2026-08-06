import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 39.760979  # Your latitude
MY_LONG = -84.192200  # Your longitude

def check_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    if MY_LAT - 5 <= iss_latitude or MY_LAT + 5 <= iss_latitude and MY_LONG - 5 <= iss_longitude or MY_LONG + 5 <= iss_longitude:
        return True
    else:
        return False

def check_time():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour in range(sunset, sunrise):
        return True
    else:
        return False

while True:
    if check_iss() and check_time():
        email = "kaylamailtesting@gmail.com"
        password = "rbljxaixsnesisgh"

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg="Subject:Check ISS\n\nLook up!")
    time.sleep(60)



