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

1. `MY_EMAIL`
* Your Gmail address that will send the emails
* 
2. `MY_PASSWORD`
*
3. `SUPABASE_CONNECTION`
* Go to your [Supabase Project](https://app.supabase.com)

Set the following secrets in your GitHub repository under Setting -> Secrets and variables -> Actions:
- `MY_EMAIL` - this is your own Gmail email.
- `MY_PASSWORD` - create app password via [myaccount.google](https://myaccount.google.com/) ->  security -> search for app-passwords -> create password -> add password here
- `SUPABASE_CONNECTION` - login to supabase -> connect -> copy session pooler -> create password -> add supabase connection here and your create supabase password

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

