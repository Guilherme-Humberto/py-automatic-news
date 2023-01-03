import time
from random import choice

import schedule

from src.config import sources
from src.start import Selenium


def startApplication(category):
    source = sources.getSource(category)
    if len(source) > 0:
        selenium = Selenium(source[0])
        print('Buscando notícias 🤟')
        selenium.run()


def job():
    category = choice(['sports', 'culture'])
    startApplication(category)


schedule.every(2).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
