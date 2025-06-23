import datetime as dt
import smtplib
from random import choice
from email.mime.text import MIMEText

QUOTE_FILE_LOCATION = 'quote.txt'
MY_EMAIL = "michael.costa594@gmail.com"
PASSWORD = 'ugnbtlxodqfyvrmo'

with open(QUOTE_FILE_LOCATION, mode='r', encoding='utf-8') as quote_file:
    quote_array = quote_file.read().split('\n')

date = dt.datetime.now()
mail_body = choice(quote_array)

message = MIMEText(mail_body)
message['Subject'] = 'Quote of the day!'

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs='azulciano57@gmail.com',
        msg=message.as_string())

