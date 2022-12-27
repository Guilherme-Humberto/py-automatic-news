from string import Template
from email.message import Message
from typing import TypedDict
from src.config import envs
from smtplib import SMTP

class EmailConfig(TypedDict):
    From: str
    To: str
    Subject: str

class SmtpServer(TypedDict):
    From: str
    To: str

class Email:
    def __init__(self, templatePath, config: EmailConfig): 
        self.templatePath = templatePath
        self.emailFrom = config['From']
        self.emailTo = config['To']
        self.emailSubject = config['Subject']

    def configEmailMessage(self, payload: str):
        message = Message()
        message['from'] = self.emailFrom
        message['to'] = self.emailTo
        message['subject'] = self.emailSubject
        message.add_header('Content-type', 'text/html')
        message.set_payload(payload)
        return message

    def createPayloadTemplate(self, newsData):
        with open(self.templatePath, 'r', encoding='utf-8') as html:
            htmlTemplate = Template(html.read())

            return htmlTemplate.safe_substitute(
                subject=self.emailSubject,
                title=newsData['title'],
                url=newsData['url']
            )

    def sendEmail(self, payloadMessage):
        with SMTP(host=envs.smtpHost, port=envs.smtpPort) as smtp:
            smtp.starttls()
            smtp.login(user=envs.emailLogin, password=envs.emailPassword)
            msg=payloadMessage.as_string().encode('utf-8')
            smtp.sendmail(from_addr=self.emailFrom, to_addrs=self.emailTo, msg=msg)