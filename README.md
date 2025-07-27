# Birthday and Wedding Email Notifier 

This is a fully automated Python project that checks a Supabase PostgreSQL database daily and sends an email when someone has a birthday or a wedding day.

## Features 

- ✅ Fetches birthday and wedding data from a Supabase PostgreSQL database
- 📧 Sends personalized emails using Gmail
- 🧠 Includes name, age calculation, and gender-based greetings
- 🕛 Automatically runs daily at 00:00 via GitHub Actions [Time Zone Info](#time-zone-info)
- 🔐 Uses GitHub Actions Secrets to keep credentials and database info secure
- 🧹 Code style checking with `flake8`

## Technology Used 
- Python 3.13
- **psycopg2** for PostgreSQL access
- **smtplib** and **email** libraries for sending emails
- **python-dotenv** and **.env** for local development
- GitHub Actions for daily scheduling
- **Supabase** (PostgreSQL database)
- **flake8** for code linting

## Installation

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

## GitHub Secrets Configuration
Before GitHub Actions can send emails and access the database, you must configure three secrets in your repository:
In this link: https://github.com/[YOUR_GITHUB_NAME]/[YOUR_PROJECT_NAME]/settings/secrets/actions you can find where to create GitHub Secrets.

1. `MY_EMAIL`
* Enter your own Gmail address that will send the emails in GitHub Secrets
2. `MY_PASSWORD`
* Create an App Password/Passkey for your Gmail account:
  * Go to [myaccount.google.com](https://myaccount.google.com/)
  * Navigate to **Security** -> **App Passwords**
  * Create a new App Password (e.g. "Birthday Notifier") and copy the password
  * Paste the password in GitHub Secrets
3. `SUPABASE_CONNECTION`
* Go to your [Supabase Project](https://app.supabase.com)
* Click **Connect**  -> **Session Pooler**
* Use the provided connection string and credentials
* Paste the connection string in GitHub Secrets

## Time Zone Info
This project uses GitHub Actions to send emails automatically every day at 22:00 **UTC**
That means:
* GitHub Actions uses **UTC** (Universal Time Coordinated) by default
* The cron schedule in the email-schedule.yml file uses: 0 22 * * *, breakdown:
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

