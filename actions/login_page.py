from selenium import webdriver
from selenium.webdriver.common.by import By
from common import input_data

def login(driver):
    data = input_data.inputs()

    driver.get("https://login.salesforce.com/")
    driver.find_element(By.ID,"username").send_keys(data['username'])
    driver.find_element(By.ID,"password").send_keys(data['password'])
    driver.find_element(By.ID,"Login").click()
