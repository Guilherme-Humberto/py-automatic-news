from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class Driver:
    def __init__(self):
        options = Options()
        options.headless = True

        self.driver = Firefox(options=options)
