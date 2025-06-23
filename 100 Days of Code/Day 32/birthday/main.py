##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
from random import randint

MY_EMAIL = "michael.costa594@gmail.com"
PASSWORD = 'ugnbtlxodqfyvrmo'

DATES_CSV_PATH = 'birthdays.csv'

dates = pandas.read_csv(DATES_CSV_PATH)

date = dt.datetime.now()
print(dates.to_dict("records"))
for item in dates.to_dict('records'):
    if item['day'] == date.day and item['month'] == date.month:
        print(f'Name: {item['name']}, birthday: {item["month"]}/{item["day"]}')
        with open(f'letter_templates/letter_{randint(1,3)}.txt', 'r') as file:
            letter = file.readlines()
            letter[0] = letter[0].replace('[NAME]', item['name'])
            letter = ''.join(letter)

with (smtplib.SMTP('smtp.gmail.com', port=587)) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs='azulciano57@gmail.com',msg=f'Subject:Happy Birthday!\n\n{letter}')
