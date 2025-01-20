import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import locators as x
from common import input_data
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then, scenarios
from selenium.webdriver.chrome.options import Options as ChromeOptions


from actions import login_page
from actions import lead_creation
from actions import lead_conversion


scenarios('../features/salesforce_2.feature')

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

@when('I am create a lead')
def lead_create(browser):
    lead_creation.create_lead(browser)


@then('I am converting the lead to account successfully by creating new account')
def convert_lead_with_newaccount(browser):
    data = input_data.inputs()
    lead_conversion.convert_lead(browser)
    try:
        time.sleep(2)
        converted=browser.find_element(By.XPATH,x.lead_convertedtitle)
        success_msg=converted.text
        expected_message=data['lead_converttitle']
        print("done: ",success_msg)
        assert success_msg == expected_message, f"Expected: '{expected_message}', but got: '{success_msg}'"

    except Exception as e:
        print(f"Error: {e}")
        raise e
