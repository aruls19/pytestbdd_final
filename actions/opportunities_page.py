import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from common import locators as x
from common import input_data
from selenium.webdriver.common.keys import Keys


def create_opportunities(driver):
    wait = WebDriverWait(driver, 30)
    data = input_data.inputs()
    actions = ActionChains(driver)
    time.sleep(10)

    opp_page=driver.find_element(By.XPATH, x.opportunites_page_button)
    actions.move_to_element(opp_page).click().perform()
    time.sleep(2)
    driver.find_element(By.XPATH, x.new_opp_button).click()
    time.sleep(2)
    driver.find_element(By.XPATH, x.opp_name_xpath).send_keys(data['new_opportunityname'])
    acc_search=driver.find_element(By.XPATH, x.search_accountname_xpath)
    acc_search.send_keys(data['new_accountname'])
    time.sleep(5)

    acc_search.send_keys(Keys.ARROW_DOWN)
    acc_search.send_keys(Keys.ARROW_DOWN)
    acc_search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, x.close_date_xpath).send_keys(data['closedate_value'])
    time.sleep(1)
    element = driver.find_element(By.XPATH, x.scroll_xpath)
    actions = ActionChains(driver)
    actions.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(5)
    stage_search = driver.find_element(By.XPATH, x.stage_xpath)
    stage_search.click()
    time.sleep(3)

    stage_search.send_keys(Keys.ARROW_DOWN)
    stage_search.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.XPATH, x.new_opp_save_button).click()

