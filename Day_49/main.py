'''
To login to Linkedin and
Find Easy Apply posts for a given job description
and to then use easy apply to send out cv
or to visit company page and follow the company
'''

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

# Grab Login and URL details from .env file
LI_USER: str = os.getenv('LI_USER')
LI_PW: str = os.getenv('LI_PASSWORD')
URL: str = os.getenv('URL')

# Set up driver and grab the URL
driver = webdriver.Firefox()
driver.get(url=URL)

# Login:
UN = driver.find_element(by=By.CSS_SELECTOR, value='#username')
PW = driver.find_element(by=By.CSS_SELECTOR, value='#password')
AD_BUTT = driver.find_element(
    by=By.CSS_SELECTOR, value='.artdeco-global-alert-action')
SI_BUTT = driver.find_element(by=By.CLASS_NAME, value='btn__primary--large')
AD_BUTT.click()
UN.send_keys(LI_USER)
PW.send_keys(LI_PW)
SI_BUTT.click()
time.sleep(30)

# Find and click through to jobs pages:
job_el = driver.find_element(By.LINK_TEXT, value='Jobs')
job_el.click()
time.sleep(30)

# Search for the jobs for Python Developer:
SRCH = driver.find_element(
    By.XPATH, '//*[starts-with(@id, "jobs-search-box")]')
SRCH.clear()
SRCH.send_keys('Python Developer', Keys.ENTER)
time.sleep(25)

# Find Easy Apply jobs only:
# driver.find_element(By.XPATH, "//button[contains(text(),'Easy Apply')]")
