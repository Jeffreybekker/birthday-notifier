import psycopg2
import os
from datetime import datetime


conn = psycopg2.connect(os.getenv("SUPABASE_CONNECTION"))

cur = conn.cursor()
# Haalt data op van Supabase met een SQL command.
cur.execute(
    "SELECT voornaam, huwelijksdatum, geboortedatum FROM familiegegevens;"
    )
rows = cur.fetchall()

today = datetime.today().date()


def krijg_verjaardag_vandaag():
    for row in rows:
        voornaam, geboortedatum = row

        if geboortedatum and geboortedatum.month == today.month and geboortedatum.day == today.day:
            return voornaam


def krijg_huwelijk_vandaag():
    for row in rows:
        voornaam, huwelijksdatum = row
        if huwelijksdatum and huwelijksdatum.month == today.month and huwelijksdatum.day == today.day:
            naam = voornaam


cur.close()
conn.close()
