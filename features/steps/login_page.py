from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open the main page')
def open_reelly_login_page(context):
    context.app.login_page.go_to_login_page()

@when("Click continue button after filling credentials")
def perform_login(context):
    context.app.login_page.fill_login_form()

@then("Verify logo is visible in home page")
def verify_login(context):
    context.app.login_page.verify_login()