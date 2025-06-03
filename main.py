import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.getenv("SUPABASE_CONNECTION"))

cur = conn.cursor()
cur.execute("SELECT voornaam, huwelijksdatum, geboortedatum FROM familiegegevens;") # Haalt de data op van Supabase. 
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
