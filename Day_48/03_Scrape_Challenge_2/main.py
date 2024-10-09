'''
To scrape some details from
The Wikipedia page
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

URL = r'https://en.wikipedia.org/wiki/Main_Page'

driver.get(url=URL)

number = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')

print(number.text)

# Click on the anchor to navigate to the page

# number.click()

# driver.close()

# Click by finding link text

# all_portals = driver.find_element(by=By.LINK_TEXT, value='Content portals')
# all_portals.click()

# type to webpage

search = driver.find_element(by=By.NAME, value='search')
search.send_keys('Python', Keys.ENTER)
