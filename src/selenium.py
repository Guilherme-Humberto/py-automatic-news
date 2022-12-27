def culture(): print('culture')
def policy(): print('policy')

from src.news.sports import SportNews
from src.email import email
from src.config.email import emailConfig, templatePath

class Selenium:
    def __init__(self, source):
        self.category = source['category']
        self.url = source['url']

    def run(self):
        if self.category == 'sports': 
            sportNews = SportNews(self.url)
            sportNews.run()

            emailConfig['Subject'] = self.category
            
            sender = email.Email(templatePath, emailConfig)
            for newData in sportNews.news:
                payload = sender.createPayloadTemplate(newData)
                emailMessage = sender.configEmailMessage(payload)
                sender.sendEmail(emailMessage)

            return None

        if self.category == 'culture': return culture()
        if self.category == 'policy': return policy()