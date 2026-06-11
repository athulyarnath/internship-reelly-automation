from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from app.application import Application

BROWSERSTACK_USERNAME = "*****************"
BROWSERSTACK_ACCESS_KEY = "*****************"

def browser_init(context):
    #init_chrome(context)
    #init_firefox(context)
    init_browserstack(context)

def init_browserstack(context):
    options = Options()
    bstack_configs = {
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY,
        "browserName": "Firefox",
        "os": "Windows",
        "osVersion": "11",
        "projectName": "QAAR-1339",
        "buildName": "v1.0",
        "sessionName": "Integrate your tests with a Cloud Testing Platform",
        "seleniumVersion": "4.0.0",
        "debug": "true"
    }
    options.set_capability('bstack:options', bstack_configs)
    bstack_hub_url = f"https://hub-cloud.browserstack.com/wd/hub"

    context.driver = webdriver.Remote(command_executor=bstack_hub_url, options=options)

    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(5)
    context.wait = WebDriverWait(context.driver, timeout=20)

    context.app = Application(context.driver)
    print('Webdriver [BrowserStack] initialized')

def init_firefox(context):
    firefox_options = Options()
    firefox_options.add_argument("-headless")
    context.driver = webdriver.Firefox(options=firefox_options)

    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(5)
    context.wait = WebDriverWait(context.driver, timeout=20)

    context.app = Application(context.driver)
    print('Webdriver [Firefox] initialized')


def init_chrome(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(5)
    context.wait = WebDriverWait(context.driver, timeout=20)

    context.app = Application(context.driver)
    print('Webdriver [Chrome] initialized')


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
