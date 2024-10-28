'''
For day 50 project:
Sign in to good reads and
ADD MORE INFORMATION HERE DESCRIBE WHAT DOING
'''

from time import sleep
import os
from dotenv import load_dotenv
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
load_dotenv()
browser = webdriver.Firefox()

URL = r'https://www.goodreads.com/'
USER = os.getenv('USER')
PW = os.getenv('PWORD')

browser.get(URL)
sleep(5)
browser.find_element(by=By.LINK_TEXT, value='Sign In').click()
sleep(5)
signin = browser.find_elements(
    By.TAG_NAME, 'button')
signin = signin[-1]
signin.click()
sleep(5)
browser.find_element(by=By.ID, value='ap_email').send_keys(USER)
browser.find_element(by=By.ID, value='ap_password').send_keys(PW)
browser.find_element(by=By.ID, value='signInSubmit').click()
sleep(5)
# browser.find_element(by=By.LINK_TEXT, value='Lists').click()
