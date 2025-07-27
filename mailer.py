import smtplib
import os
from email.mime.text import MIMEText
from main import krijg_huwelijk_vandaag, krijg_verjaardag_vandaag


def send_email_jarige():
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    result = krijg_verjaardag_vandaag()

    if not result:
        print("Niemand jarig vandaag. Geen e-mail verzonden.")
        return

    voornaam, leeftijd, geslacht = result

    if geslacht == "Man":
        man_of_vrouw = "hij"
        hem_of_haar = "hem"
    elif geslacht == "Vrouw":
        man_of_vrouw = "ze"
        hem_of_haar = "haar"

    msg = MIMEText(f"Het is {voornaam}'s verjaardag"
                   f' en {man_of_vrouw} is {leeftijd} jaar oud geworden! '
                   f'Stuur {hem_of_haar} vandaag nog een berichtje!')
    msg['Subject'] = f'{voornaam} is jarig vandaag!'
    msg['From'] = my_email
    msg['To'] = my_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(my_email, my_password)
        server.send_message(msg)

        print("E-mail is verzonden!")


def send_email_huwelijk():
    my_email = os.getenv("MY_EMAIL")
    my_password = os.getenv("MY_PASSWORD")

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    result = krijg_huwelijk_vandaag()

    if not result:
        print("Geen trouwdagen vandaag. Geen e-mail verzonden.")
        return

    voornaam, aantal, geslacht = result

    if geslacht == "Man":
        man_of_vrouw = "hij"
        hem_of_haar = "hem"
    elif geslacht == "Vrouw":
        man_of_vrouw = "ze"
        hem_of_haar = "haar"

    msg = MIMEText(f'Het is de trouwdag van {voornaam}'
                   f' en {man_of_vrouw} is al {aantal} jaar getrouwd! '
                   f'Stuur {hem_of_haar} vandaag nog een berichtje!')
    msg['Subject'] = f"Het is {voornaam}'s trouwdag!!"
    msg['From'] = my_email
    msg['To'] = my_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(my_email, my_password)
    server.send_message(msg)
    server.quit()

    print("E-mail is verzonden!")


send_email_jarige()
send_email_huwelijk()
