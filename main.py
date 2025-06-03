import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

conn = psycopg2.connect(os.getenv("SUPABASE_CONNECTION"))

cur = conn.cursor()
# Haalt data op van Supabase met een SQL command.
cur.execute(
    "SELECT voornaam, huwelijksdatum, geboortedatum FROM familiegegevens;"
    )
rows = cur.fetchall()

today = datetime.today().date()

for row in rows:
    voornaam, huwelijksdatum, geboortedatum = row

    if geboortedatum and geboortedatum.month == today.month and geboortedatum.day == today.day:
        naam = voornaam

    if huwelijksdatum and huwelijksdatum.month == today.month and huwelijksdatum.day == today.day:
        naam = voornaam

cur.close()
conn.close()
