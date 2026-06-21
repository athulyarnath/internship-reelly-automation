from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class Application:
    def __init__(self, context):
        self.driver = context.driver
        self.DEVICE = context.DEVICE

        self.page = BasePage(context)

        self.login_page = LoginPage(self.page)
        self.home_page = HomePage(self.page)
