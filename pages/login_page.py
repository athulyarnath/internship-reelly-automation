from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    FLD_EMAIL = (By.CSS_SELECTOR, '[id="email-2"]')
    FLD_PWORD = (By.CSS_SELECTOR, '[id="field"]')
    BUT_CONTINUE = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
    LOGO_HMPAGE = (By.CSS_SELECTOR, 'img[alt="logo"]')

    USERNAME_VAL = "athulyarnath@gmail.com"
    PASSWORD_VAL = "Rpassword1."

    MAIN_URL = "https://soft.reelly.io/sign-in"

    def go_to_login_page(self):
        self.open(self.MAIN_URL)

    def fill_login_form(self):
        sleep(3)
        self.set_text(*self.FLD_EMAIL, text=self.USERNAME_VAL)
        self.set_text(*self.FLD_PWORD, text=self.PASSWORD_VAL)
        self.click(*self.BUT_CONTINUE)


    def verify_login(self):
        logo = self.find_element(*self.LOGO_HMPAGE)
        if not logo.is_displayed():
            assert False
