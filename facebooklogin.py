from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys



path = Service(executable_path="/opt/google/chrome/chromedriver")
driver = webdriver.Chrome(service = path)
# driver.maximize_window()
driver.get("https://www.messenger.com")
time.sleep(1)

#your username goes here
driver.find_element(By.NAME, "email").send_keys("-----")
time.sleep(0.1)

#your password goes here
driver.find_element(By.NAME, "pass").send_keys("------")
time.sleep(0.1)

driver.find_element(By.NAME, "login").click()
time.sleep(0.1)
# driver.find_element(By.XPATH, "//button[text()='").click()
driver.find_element(By.LINK_TEXT, "Continue").click()
time.sleep(0.1)

# two factor authentication goes here
driver.find_element(By.NAME, "approvals_code").send_keys("xxxxxx")
time.sleep(0.1)

driver.find_element(By.ID, "checkpointSubmitButton").click()
time.sleep(0.1)

driver.find_element(By.NAME, "name_action_selected").click()
time.sleep(0.1)
driver.find_element(By.ID, "checkpointSubmitButton").click()
time.sleep(0.1)
driver.find_element(By.ID, "checkpointSubmitButton").click()
time.sleep(1)
driver.find_element(By.ID, "checkpointSubmitButton").click()
time.sleep(1)
driver.find_element(By.NAME, "name_action_selected").click()
time.sleep(0.1)
driver.find_element(By.ID, "checkpointSubmitButton").click()
time.sleep(0.1)