import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common import locators as x
from common import input_data
from selenium.webdriver.common.keys import Keys


def create_account(driver):
    data = input_data.inputs()
    time.sleep(5)
    actions = ActionChains(driver)

    acc_page=driver.find_element(By.XPATH, x.account_page_button)
    actions.move_to_element(acc_page).click().perform()
    time.sleep(3)

    driver.find_element(By.XPATH, x.new_account_button).click()
    time.sleep(2)
    driver.find_element(By.XPATH, x.create_accountname).send_keys(data['new_accountname'])
    driver.find_element(By.XPATH, x.create_account_save_button).click()


def back_to_account(driver):

    data = input_data.inputs()
    actions = ActionChains(driver)
    time.sleep(6)

    acc_page=driver.find_element(By.XPATH, x.account_page_button)
    actions.move_to_element(acc_page).click().perform()
    time.sleep(3)

    driver.find_element(By.XPATH, x.first_account_xpath).click()
    element = driver.find_element(By.XPATH, x.scroll)
    actions = ActionChains(driver)
    actions.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(5)

