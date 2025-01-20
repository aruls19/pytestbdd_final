import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from common import locators as x
from common import input_data
from selenium.webdriver.common.keys import Keys


def create_contact(driver):
    wait = WebDriverWait(driver, 30)
    data = input_data.inputs()
    actions = ActionChains(driver)
    time.sleep(5)

    contact_page=driver.find_element(By.XPATH, x.contact_page_button)
    actions.move_to_element(contact_page).click().perform()
    time.sleep(3)
    driver.find_element(By.XPATH, x.new_contact_button).click()
    time.sleep(2)
    driver.find_element(By.XPATH, x.contact_firstname).send_keys(data['contact_firstname_value'])
    driver.find_element(By.XPATH, x.contact_lastname).send_keys(data['contact_lastname_value'])
    acc_search=driver.find_element(By.XPATH, x.search_accountname_xpath)
    acc_search.send_keys(data['new_accountname'])
    time.sleep(5)

    acc_search.send_keys(Keys.ARROW_DOWN)
    acc_search.send_keys(Keys.ARROW_DOWN)
    acc_search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, x.new_contact_save_button).click()

