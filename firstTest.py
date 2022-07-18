from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


path = Service(executable_path="/opt/google/chrome/chromedriver")
driver = webdriver.Chrome(service=path)

driver.maximize_window()
driver.get("https://www.google.com")
# time.sleep(2)

# driver.find_element(By.NAME, 'q').send_keys('black paper')
# insted of above code below is better.
driver.find_element (By.XPATH, "//input[@maxlength='2048']").send_keys('shit')
time.sleep(1)

driver.find_element(By.NAME, 'btnK').click()
time.sleep(5)


# driver.close()

print("first test case created successfully")
