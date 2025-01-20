from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import locators as x
from common import input_data


def create_lead(driver):
    wait = WebDriverWait(driver, 30)
    data=input_data.inputs()

    wait.until(EC.presence_of_element_located((By.XPATH, x.lead_pagetitle)))

    driver.find_element(By.XPATH, x.lead_new_button).click()
    wait.until(EC.presence_of_element_located((By.XPATH, x.new_lead_window)))
    time.sleep(2)
    driver.find_element(By.XPATH, x.lead_firstname).send_keys(data['lead_firstname_value'])
    driver.find_element(By.XPATH, x.lead_lastname).send_keys(data['lead_lastname_value'])
    driver.find_element(By.XPATH, x.lead_companyname).send_keys(data['lead_companyname_value'])
    driver.find_element(By.XPATH, x.lead_savebutton).click()
