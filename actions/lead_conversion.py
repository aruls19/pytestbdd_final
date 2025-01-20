import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import locators as x
from common import input_data
from selenium.webdriver.common.keys import Keys


def convert_lead(driver):
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.XPATH, x.leadpage_convertbutton)))
    time.sleep(3)
    driver.find_element(By.XPATH, x.leadpage_convertbutton).click()
    wait.until(EC.presence_of_element_located((By.XPATH, x.lead_convertwindow)))
    time.sleep(3)
    driver.find_element(By.XPATH, x.leadtoaccount_convert_button).click()

def convert_lead_existing(driver):
    wait = WebDriverWait(driver, 30)
    data = input_data.inputs()

    wait.until(EC.presence_of_element_located((By.XPATH, x.leadpage_convertbutton)))
    driver.find_element(By.XPATH, x.leadpage_convertbutton).click()
    wait.until(EC.presence_of_element_located((By.XPATH, x.lead_convertwindow)))
    time.sleep(3)
    exist_button=driver.find_element(By.XPATH, x.leadconvert_existingbutton)
    exist_button.click()
    search_box=driver.find_element(By.XPATH, x.leadconvert_accountsearch)
    search_box.send_keys(data['accountsearch'])
    time.sleep(5)

    search_box.send_keys(Keys.ARROW_DOWN)
    search_box.send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, x.searchaccount_select).click()
    time.sleep(2)

    driver.find_element(By.XPATH, x.leadtoaccount_convert_button).click()


def goto_lead(driver):
    driver.find_element(By.XPATH, x.gotolead_button).click()
    time.sleep(5)

