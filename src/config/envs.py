import os

from dotenv import load_dotenv

load_dotenv()

smtpPort = os.getenv("SMTP_PORT")
smtpHost = os.getenv("SMTP_HOST")
emailLogin = os.getenv("EMAIL_LOGIN")
emailPassword = os.getenv("EMAIL_PASSWORD")
emailTo = os.getenv("EMAIL_TO")

basePath = r"./src/email/html/base.html"
templatePath = r"./src/email/html/email.html"
emailConfig = {"From": emailLogin, "To": emailTo}
