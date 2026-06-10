from behave import given, when, then
from selenium.webdriver.common.by import By


@when("Click on “market” in the left side menu.")
def click_on_market_menu(context):
    context.app.home_page.click_on_market_menu()

@then("Verify the right page opens")
def verify_right_page(context):
    context.app.home_page.verify_right_page()

@when("Click on “Agent” filter at the top of the page")
def click_on_agent_filter(context):
    context.app.home_page.click_on_agent_filter()

@then("Verify that all results shown have the “Agent” tag.")
def verify_agent_tag(context):
    context.app.home_page.verify_agent_tag()
