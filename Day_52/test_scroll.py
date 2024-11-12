from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://yahoo.com')
driver.implicitly_wait(15)
# driver.find_element(By.TAG_NAME, 'button').click()
but = driver.find_element(By.TAG_NAME, 'button')
driver.execute_script("arguments[0].scrollIntoView(true);", but)
sleep(15)
driver.find_elements(By.TAG_NAME, 'button')[1].click()
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, 500);")
