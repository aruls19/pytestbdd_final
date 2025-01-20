import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import locators as x
from common import input_data
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then, scenarios, scenario
from selenium.webdriver.chrome.options import Options as ChromeOptions

from actions import login_page
from actions import account_creation
from actions import contact_page
from actions import opportunities_page

scenarios('../features/salesforce_3.feature')

@pytest.fixture
def browser():
    # Setup for browser fixture
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(options=chrome_options)
    print("Launching Chrome browser with notifications disabled")
    driver.maximize_window()

    yield driver
    driver.quit()

@given('I am logged in to salesforce')
def login_salesforce(browser):
    login_page.login(browser)

@when('I am create an account')
def create_account(browser):
    account_creation.create_account(browser)

@when('create contact and attach to created account')
def create_contact_and_attach(browser):
    contact_page.create_contact(browser)

@when('create opportunity and attach to created account')
def create_opportunity_and_attach(browser):
    opportunities_page.create_opportunities(browser)

@then('Contact and opportunity should successfully attached with account')
def verify_account_page(browser):
    account_creation.back_to_account(browser)
    data=input_data.inputs()

    try:
        time.sleep(2)
        attached_contact_name = browser.find_element(By.XPATH, x.contact_name.replace('CNAME',data['contact_firstname_value']))
        attached_opp_name = browser.find_element(By.XPATH, x.opportunities_name.replace('ONAME',data['new_opportunityname']))
        contact_name = attached_contact_name.text
        opp_name = attached_opp_name.text
        expected_contact_name = data['contact_firstname_value']
        expected_opp_name = data['new_opportunityname']
        print("done: ", contact_name,opp_name)
        assert expected_contact_name in contact_name, f"Expected: '{expected_contact_name}', but got: '{contact_name}'"
        assert expected_opp_name in opp_name, f"Expected: '{expected_opp_name}', but got: '{opp_name}'"

    except Exception as e:
        print(f"Error: {e}")
        raise e
