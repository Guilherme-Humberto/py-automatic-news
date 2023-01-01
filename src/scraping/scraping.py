from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


class WebScraping:
    def __init__(self, url):
        self.url = url
        self.posts = []
        self.driver = Firefox()

    def findElements(self, by, ref, element):
        try:
            return ref.find_elements(by, element)
        except NoSuchElementException:
            print(f"{element} does not exist")
            return False

    def findElement(self, by, ref, element):
        try:
            return ref.find_element(by, element)
        except NoSuchElementException:
            print(f"{element} does not exist")
            return False

    def run(self):
        self.driver.get(self.url)
        elements = self.findElements(
            by=By.CLASS_NAME,
            ref=self.driver,
            element='feed-post-body'
        )

        counter = 0
        limit = 5

        while counter < limit:
            counter = counter + 1
            element = elements[counter]

            refElement = self.findElement(
                by=By.CLASS_NAME,
                ref=element,
                element='feed-post-link'
            )
            excerptElement = self.findElement(
                by=By.CLASS_NAME,
                ref=element,
                element='feed-post-body-resumo'
            )
            hrefPost = refElement.get_attribute('href')

            if not excerptElement:
                excerptPost = ''
            else:
                excerptPost = excerptElement.text

            self.posts.append({
                'url': hrefPost,
                'title': refElement.text,
                'excerpt': excerptPost
            })

    def close(self):
        self.driver.close()
        return
