import smtplib
import os
from email.mime.text import MIMEText




def send_email():
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEText('Het is de verjaardag van (naam),'
                   ' stuur hem of haar vandaag nog een berichtje!')
    msg['Subject'] = '(Naam) is jarig vandaag!'
    msg['From'] = my_email
    msg['To'] = my_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(my_email, my_password)
    server.send_message(msg)
    server.quit()

    print("E-mail is verzonden!")


send_email()
