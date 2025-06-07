# Birthday and Wedding Email Notifier 🥳🎂👰🏻🤵🏻‍♂️

This Python project automatically sends a birthday and/or wedding e-mail every day at midnight, based on the data stored in a Supabase PostgreSQL database. It runs fully automated via GitHub Actions.

## Features 🚀

- Fetches birthday and weddingday data from a Supabase Database
- Sends an email if someone has their birtday or wedding
- Includes personalized name, gender-based salution and age
- Automatically runs daily at 00:00 via GitHub Actions
- Keeps email credentials and database secrets secure via GitHub Actions

## Technology Used ⚙️🛠️

- Python 3.13
- `psycopg2` for PostgreSQL database acces
- `smtplib` and `email` for sending emails
- `python-dotenv` for local development
- GitHub Actions for automation
- Supabase (PostgreSQL)

## Secrets configuration 🔐
Set the following secrets in your GitHub repository under Setting -> Secrets and variables -> Actions:
- `MY_EMAIL` - 
- `MY_PASSWORD` - 
- `SUPABASE_CONNECTION` - 
