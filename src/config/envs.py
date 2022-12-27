import os
from dotenv import load_dotenv

load_dotenv()

smtpPort = os.getenv("SMTP_PORT")
smtpHost = os.getenv("SMTP_HOST")
emailLogin = os.getenv("EMAIL_LOGIN")
emailPassword = os.getenv("EMAIL_PASSWORD")