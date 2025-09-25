import requests
from datetime import datetime
from tkinter import messagebox
import smtplib

MY_EMAIL = "michael.costa594@gmail.com"
PASSWORD = 'ugnbtlxodqfyvrmo'

MY_LONG = -47.216155
MY_LAT = -23.112449


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

is_iss_lat_close = MY_LAT - iss_latitude > -5 and MY_LAT - iss_latitude < 5 or iss_latitude - MY_LAT > -5 and iss_latitude - MY_LAT < 5
is_iss_long_close = MY_LONG - iss_longitude > -5 and MY_LONG - iss_longitude < 5 or iss_longitude - MY_LONG > -5 and iss_longitude - MY_LONG < 5
is_iss_close = is_iss_long_close and is_iss_lat_close

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
is_night = time_now.hour >= sunset and time_now.hour <= sunrise

if is_night and is_iss_close:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='azulciano57@gmail.com', msg='Subject:look up\n\niss is close')
    messagebox.showinfo('Email sent!', 'look up email sent.')
else:
    messagebox.showerror('Iss might be far...', 'mail has not been sent.')
