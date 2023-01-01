from random import choice

from src.config import sources
from src.start import Selenium


def start(category):
    source = sources.getSource(category)
    if len(source) > 0:
        selenium = Selenium(source[0])
        selenium.run()


category = choice(['sports', 'culture'])
start(category)
