import smtplib


MY_EMAIL = "michael.costa594@gmail.com"
PASSWORD = 'ugnbtlxodqfyvrmo'

with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs='azulciano57@gmail.com',
                        msg='Subject: Hi!\n\nEmail body.')

