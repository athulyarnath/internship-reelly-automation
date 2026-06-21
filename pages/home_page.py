from time import sleep

from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class HomePage(BasePage):
    BTN_MARKET = (By.CSS_SELECTOR, '[aria-label="Market"]')
    DIV_HEADER = (By.CSS_SELECTOR, 'div[class*="new-market-h1"]')

    BTN_AGENT = (By.CSS_SELECTOR, 'div[wized="servicesOffersFilterAgent"]')
    TAB_OFFERS = (By.CSS_SELECTOR, 'div[class="w-layout-grid new-market-offers-grid"]')
    TAG_AGENTS = (By.CSS_SELECTOR, 'div[w-el-text="For agency"]')

    DEVICE = BasePage.DEVICE

    def click_on_market_menu(self):
        if self.DEVICE == "Mobile":
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="email-2"]').send_keys(self.USERNAME_VAL)
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="field"]').send_keys(self.PASSWORD_VAL)
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Continue"]').click()
        else:
            self.click(*self.BTN_MARKET)
        sleep(1)

    def verify_right_page(self):
        dheader = self.find_element(*self.DIV_HEADER)

        if dheader is None:
            assert False

    def click_on_agent_filter(self):
        self.click(*self.BTN_AGENT)

    def verify_agent_tag(self):
        sleep(3)
        offer_grid = self.find_element(*self.TAB_OFFERS)
        agent_tags = offer_grid.find_elements(*self.TAG_AGENTS)

        if agent_tags is None:
            assert False
        else:
            tag_cnt = len(agent_tags)
            agent_cnt = 0
            for tag in agent_tags:
                if tag is not None and tag.get_attribute('innerHTML') == "Agent":
                    agent_cnt += 1
                    print(tag.get_attribute('innerHTML'))

            assert agent_cnt == tag_cnt
