import psycopg2
import os
from datetime import datetime
from zoneinfo import ZoneInfo

try:
    conn = psycopg2.connect(os.getenv("SUPABASE_CONNECTION"))

    cur = conn.cursor()
    # Haalt data op van Supabase met een SQL command.
    cur.execute(
        "SELECT voornaam, huwelijksdatum, geboortedatum, geslacht FROM familiegegevens;"
        )
    rows = cur.fetchall()

except Exception as e:
    print(f"Databaseverbinding of query mislukt: {e}")
    exit()

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()

today = datetime.now(ZoneInfo("Europe/Amsterdam")).date()


def krijg_verjaardag_vandaag():
    for row in rows:
        voornaam, huwgeboortedatum, geboortedatum, geslacht = row

        if geboortedatum and geboortedatum.month == today.month and geboortedatum.day == today.day:
            leeftijd = today.year - geboortedatum.year
            return voornaam, leeftijd, geslacht


def krijg_huwelijk_vandaag():
    for row in rows:
        voornaam, huwelijksdatum, geboortedatum, geslacht = row
        if huwelijksdatum and huwelijksdatum.month == today.month and huwelijksdatum.day == today.day:
            aantal = today.year - huwelijksdatum.year
            return voornaam, aantal, geslacht
