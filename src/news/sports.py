from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class SportNews:
    def __init__(self, url):
        self.url = url
        self.driver = Chrome(executable_path="./chromedriver.exe")
        self.news = []

    def run(self):
        self.driver.get(self.url)
        elements = self.driver.find_elements(By.CLASS_NAME, 'feed-post-body')
        for element in elements:
            refElement = element.find_element(By.CLASS_NAME, 'feed-post-link')
            hrefPost = refElement.get_attribute('href')
            self.news.append({ 'url': hrefPost, 'title': refElement.text })

        return None