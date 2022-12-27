from src.selenium import Selenium
from src.sources import getSourceByCategory
from random import choice

def start(category):
    source = getSourceByCategory(category)
    if len(source) > 0: 
        selenium = Selenium(source[0])
        selenium.run()

category = choice([
    'sports', 
    'culture', 
    'policy'
])
start(category)