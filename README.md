# Birthday and Wedding Email Notifier 

This is a fully automated Python project that checks a Supabase PostgreSQL database daily and sends an email when someone has a birthday or a wedding day.

## ✅ Features 

- 🔎 Fetches birthday and wedding data from a Supabase PostgreSQL database
- 📧 Sends personalized emails using Gmail
- 🧠 Includes name, age calculation, and gender-based greetings
- 🕛 Automatically runs daily at 00:00 via GitHub Actions [Time Zone Info](#time-zone-info)
- 🔐 Uses GitHub Actions Secrets to keep credentials and database info secure
- 🧹 Code style checking with `flake8`

⚠️ **Note:** The project is written in **Dutch**, both in terms of **column names** (e.g., voornaam, geboortedatum, geslacht) and **variable names** in the code.
If you prefer to use English, you'll need to update both the **database column names and the Python code** accordingly.

## ✉️ Example Email Output
<img width="1200" alt="image" src="https://github.com/user-attachments/assets/5c5ab8fa-67fa-4f49-8922-f25a0752fcea" /> 

**Translated** <br>
**Title**: _It is Jeffreys birthday today!_ <br>
**Message**: _It is Jeffreys birthday and he just turned 27! Send him a message today!_

## 🛠️ Technology Used 
- Python 3.13
- **psycopg2** for PostgreSQL access
- **smtplib** and **email** libraries for sending emails
- **python-dotenv** and **.env** for local development
- GitHub Actions for daily running script
- **Supabase** (PostgreSQL database)
- **flake8** for code linting

## 🧾 Database Setup (Supabase Table)
⚠️ **Note**: the project itself is written in Dutch terms. You can change it to English if you like, but you must change the column names aswel!
Your Supabase PostgreSQL database must contain a single table with the following structure:

### 📊 Required Table: `familiegegevens`
| Column Name    | Type      | Description                            |
|----------------|-----------|----------------------------------------|
| `voornaam`   | `text`    | Person's first name                    |
| `achternaam`    | `text`    | Person's last name                     |
| `geslacht`       | `text`    | Either `"man"` or `"vrouw"`         |
| `geboortedatum `   | `date`    | Birthday in format `YYYY-MM-DD`       |
| `huwelijksdatum ` | `date`    | Wedding date in format `YYYY-MM-DD` (can be `NULL`) |

⚠️ Make sure that all dates use the `YYYY-MM-DD` format.

### 🛠️ Create the Table (SQL)

```
CREATE TABLE familiegegevens (
    voornaam VARCHAR(128) NOT NULL,
    achternaam VARCHAR(128) NOT NULL,
    geslacht VARCHAR(16) NOT NULL,
    huwelijksdatum DATE,
    geboortedatum DATE,
);
```

### 🧪 Example rows
```
INSERT INTO familiegegevens (voornaam, achternaam, geslacht, geboortedatum , huwelijksdatum )
VALUES ('Jeffrey', 'Bekker', 'man', '1997-07-27', '2022-08-15');

INSERT INTO familiegegevens (voornaam, achternaam, geslacht, geboortedatum , huwelijksdatum )
VALUES ('Anna', 'Jansen', 'vrouw', '1995-03-12', NULL);
```

## 🚀 Installation
1. Clone the repository:
```
git clone https://github.com/JeffreyBekker/birthday-notifier.git
```
2. Create a virtual environment:
```
python -m venv venv
```
4. Start the virtual environment, depending on your system. You can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)
5. Install dependencies:
```
pip install -r requirements.txt
```

## 🔐 GitHub Secrets Configuration
Before GitHub Actions can send emails and access the database, you must configure three secrets in your repository:
You can add them here: https://github.com/[YOUR_GITHUB_USERNAME]/[YOUR_PROJECT_NAME]/settings/secrets/actions

1. `MY_EMAIL`
* Your own Gmail address that will send the emails
* Add it to GitHub Secrets under the name MY_EMAIL
2. `MY_PASSWORD`
This is a Gmail App Password (not your regular Gmail password)<br>
To create it:
* Go to [myaccount.google.com](https://myaccount.google.com/)
* Navigate to **Security** -> **App Passwords**
* Create a new App Password (e.g. "Birthday Notifier")
* Copy the generated Passkey
* Add it to GitHub Secrets as MY_PASSWORD
3. `SUPABASE_CONNECTION`
* Go to your [Supabase Project](https://app.supabase.com)
* Click **Connect**  -> **Session Pooler**
* Use the provided connection string and credentials
* Add it to GitHub Secrets as SUPABASE_CONNECTION

**It should look like this:** <br>
<img width="800" alt="image" src="https://github.com/user-attachments/assets/5155bbe1-b403-443c-9ac7-e4f64e2f90c6" />

## ⏰ Time Zone Info
This project uses GitHub Actions to send emails automatically every day at 22:00 **UTC**
That means:
* GitHub Actions uses **UTC** (Universal Time Coordinated) by default
* The cron schedule in the email-schedule.yml file uses: 0 22 * * *. Breakdown:
  * 0 = minutes (xx:00)
  * 22 = 22 hours (22:xx)
  * The other bullets mean: day of the month, month, day of the week

### Adjusting to Your Local Time
To run this script at your preferred **local time**, follow these steps:

1. Decide the time you want the email to be sent (e.g. 00:00 local time).
2. Convert your local time to **UTC** using tools like:
   - [https://www.timeanddate.com/worldclock/converter.html](https://www.timeanddate.com/worldclock/converter.html)
   - Google: “00:00 CEST to UTC”
3. Update the cron in `.github/workflows/email-schedule.yml`

For example:
- You want **00:00 EDT** (Eastern Daylight Time, New York)
- EDT = UTC-4 → 00:00 becomes **04:00 UTC**
- Your cron becomes:

```yaml
schedule:
  - cron: "0 4 * * *"
