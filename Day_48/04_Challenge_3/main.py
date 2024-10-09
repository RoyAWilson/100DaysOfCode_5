'''
Challenge: Fill out and send online form on test website built for course
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

URL = r'http://secure-retreat-92358.herokuapp.com/'

driver.get(url=URL)

box = driver.find_element(by=By.NAME, value='fName')
box.send_keys('Roy', Keys.TAB, 'Wilson', Keys.TAB,
              'roywilson@myip.com', Keys.ENTER)
