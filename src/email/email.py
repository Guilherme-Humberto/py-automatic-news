from email.message import Message
from smtplib import SMTP
from string import Template

from src.config import envs


class Email:
    def __init__(self, templatePath, config):
        self.templatePath = templatePath
        self.emailFrom = config['From']
        self.emailTo = config['To']
        self.emailSubject = config['Subject']

    def configBaseHtmlTemplate(self, emailBody):
        with open(envs.basePath, 'r', encoding='utf-8') as html:
            htmlTemplate = Template(html.read())
            return htmlTemplate.safe_substitute(email=emailBody)

    def configEmailMessage(self, payload: str):
        message = Message()
        message['from'] = self.emailFrom
        message['to'] = self.emailTo
        message['subject'] = self.emailSubject
        message.add_header('Content-type', 'text/html')
        message.set_payload(payload)
        return message

    def createEmailHtmlTemplate(self, postData):
        with open(self.templatePath, 'r', encoding='utf-8') as html:
            htmlTemplate = Template(html.read())

            return htmlTemplate.safe_substitute(
                subject=self.emailSubject,
                title=postData['title'],
                url=postData['url'],
                excerpt=postData['excerpt']
            )

    def sendEmail(self, payload):
        with SMTP(host=envs.smtpHost, port=envs.smtpPort) as smtp:
            smtp.starttls()
            smtp.login(user=envs.emailLogin, password=envs.emailPassword)
            msg = payload.as_string().encode('utf-8')
            smtp.sendmail(
                msg=msg,
                to_addrs=self.emailTo,
                from_addr=self.emailFrom
            )
            print('Email enviado com sucesso!! 🚀')
