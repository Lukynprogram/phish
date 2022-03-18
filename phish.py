#!/bin/python3
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Definovani zakladnich parametru
receiver_email = "komu"
sent_from = "odkoho"
message = MIMEMultipart("alternative")
message["Subject"] = "subject"
message["From"] = "odkoho <odkoho@odkoho>"
message["To"] = receiver_email

#Obsah zpravy
text = f"""\
Dobrý den, 

toto je obsah podvrženého mailu.

Přeji krásný zbytek dne,
LJ.
"""

part1 = MIMEText(text, "plain")
message.attach(part1)

context = ssl.create_default_context()
try:
        server = smtplib.SMTP_SSL('VASSMTPSERVER', ČÍSLOPORTU)
        server.ehlo()
        server.login("login", "hesla")
        server.sendmail(sent_from, receiver_email, message.as_string())
        server.close()

        print('Email sent!')

except Exception as exception:
    print(exception)
    print('Something went wrong...')
