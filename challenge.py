import smtplib
import datetime as dt
import random
from config import MY_EMAIL, MY_PASSWORD

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes).strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivational Email!\n\n{quote.encode("utf-8")}"
        )
