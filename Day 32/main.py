import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day = now.weekday()
chosen_quote = ""

if day == 5:
    with open(file="quotes.txt", mode="r") as file:
        quotes = file.readlines()
    chosen_quote = random.choice(quotes)

    email = "kaylamailtesting@gmail.com"
    password = "rbljxaixsnesisgh"

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="kaylamailtesting@yahoo.com",
                            msg=f"Subject:Motivational Quote Saturday!\n\n{chosen_quote}")





