from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.page = BasePage(driver)
        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)
