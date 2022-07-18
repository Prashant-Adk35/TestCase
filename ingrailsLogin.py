from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="/opt/google/chrome/chromedriver")


driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://www.ingrails.com/school")
time.sleep(0.1)

driver.find_element(By.NAME, "email").send_keys("xxxx")
time.sleep(0.1)

driver.find_element(By.NAME, "password").send_keys("xxxx")
time.sleep(0.1)

driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
time.sleep(0.1)
