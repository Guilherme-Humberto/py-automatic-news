from src.config import envs
from src.email import email
from src.scraping.scraping import WebScraping


class Selenium:
    def __init__(self, source):
        self.category = source['category']
        self.url = source['url']

    def message(self, sender, posts):
        emailTemplate = ''
        for post in posts:
            postData = sender.createEmailHtmlTemplate(post)
            emailTemplate += postData

        baseTemplate = sender.configBaseHtmlTemplate(emailTemplate)
        emailMassage = sender.configEmailMessage(baseTemplate)
        return sender.sendEmail(emailMassage)

    def run(self):
        scraping = WebScraping(self.url)
        scraping.run()

        envs.emailConfig['Subject'] = self.category
        sender = email.Email(
            config=envs.emailConfig,
            templatePath=envs.templatePath,
        )

        self.message(sender, scraping.posts)
        return scraping.close()
