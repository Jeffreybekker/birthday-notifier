import smtplib
import os
from email.mime.text import MIMEText
from main import krijg_verjaardag_vandaag


def send_email():
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    voornaam = krijg_verjaardag_vandaag
    msg = MIMEText(f'Het is de verjaardag van {voornaam},'
                   ' stuur hem of haar vandaag nog een berichtje!')
    msg['Subject'] = f'{voornaam} is jarig vandaag!'
    msg['From'] = my_email
    msg['To'] = my_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(my_email, my_password)
    server.send_message(msg)
    server.quit()

    print("E-mail is verzonden!")


send_email()
