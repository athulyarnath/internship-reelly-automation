from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def set_text(self, *locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def set_text_go(self, *locator, text):
        field = self.driver.find_element(*locator)
        field.send_keys(text)
        field.send_keys(Keys.RETURN)