'''
Use Selenium to play the cookie clicking game
using the traditional version of the game
URL: http://orteil.dashnet.org/experiments/cookie/
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

URL = r'http://orteil.dashnet.org/experiments/cookie/'

driver.get(url=URL)


def click_cookie() -> None:
    '''
    Click on the cookie multiple tiems
    for 5 seconds
    '''

    start_time = time.time()
    COOKIE = driver.find_element(by=By.CSS_SELECTOR, value='#cookie')
    while time.time() - start_time < 5:
        COOKIE.click()
    affordable(driver, price_list)


def affordable(driv, prices: list):
    '''
    Check if can afford any of the
    specials from right hand side
    '''
    n_cookies = driver.find_element(by=By.CSS_SELECTOR, value='#money')
    if int(n_cookies.text) >= prices[-1]:
        timeM_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyTime\ machine > b')
        timeM_cost_el1.click()
    if int(n_cookies.text) >= prices[-2]:
        portal_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyPortal b ')
        portal_cost_el1.click()
    if int(n_cookies.text) >= prices[-3]:
        alchemy_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyAlchemy\ lab > b')
        alchemy_cost_el1.click()
    if int(n_cookies.text) >= prices[-4]:
        shipment_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyShipment b ')
        shipment_cost_el1.click()
    if int(n_cookies.text) >= prices[-5]:
        mine_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyMine b ')
        mine_cost_el1.click()
    if int(n_cookies.text) >= prices[-6]:
        factory_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyFactory b ')
        factory_cost_el1.click()
    if int(n_cookies.text) >= prices[-7]:
        grannie_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyGrandma b ')
        grannie_cost_el1.click()
    if int(n_cookies.text) >= prices[-8]:
        cursor_cost_el1 = driver.find_element(
            by=By.CSS_SELECTOR, value='#buyCursor b ')
        cursor_cost_el1.click()
    click_cookie()

# Get prices of items and add to list to pass to afford function:


price_list = []

cursor_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyCursor b ')
cursor_cost = cursor_cost_el.text.split('- ')
cursor_cost_int = int(cursor_cost[::-2][0].replace(',', ''))
price_list.append(cursor_cost_int)
grannie_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyGrandma b ')
grannie_cost = grannie_cost_el.text.split('- ')
grannie_cost_int = int(grannie_cost[::-3][0].replace(',', ''))
price_list.append(grannie_cost_int)
factory_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyFactory b ')
factory_cost = factory_cost_el.text.split('- ')
factory_cost_int = int(factory_cost[::-3][0].replace(',', ''))
price_list.append(factory_cost_int)
mine_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyMine b ')
mine_cost = mine_cost_el.text.split('- ')
mine_cost_int = int(mine_cost[::-5][0].replace(',', ''))
price_list.append(mine_cost_int)
shipment_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyShipment b ')
shipment_cost = shipment_cost_el.text.split('- ')
shipment_cost_int = int(shipment_cost[::-5][0].replace(',', ''))
price_list.append(shipment_cost_int)
alchemy_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyAlchemy\ lab > b')
alchemy_cost = alchemy_cost_el.text.split('- ')
alchemy_cost_int = int(alchemy_cost[::-6][0].replace(',', ''))
price_list.append(alchemy_cost_int)
portal_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyPortal b ')
portal_cost = portal_cost_el.text.split('- ')
portal_cost_int = int(portal_cost[::-9][0].replace(',', ''))
price_list.append(portal_cost_int)
timeM_cost_el = driver.find_element(
    by=By.CSS_SELECTOR, value='#buyTime\ machine > b')
timeM_cost = timeM_cost_el.text.split('- ')
timeM_cost_int = int(timeM_cost[::-11][0].replace(',', ''))
price_list.append(timeM_cost_int)


COOKIE = driver.find_element(by=By.CSS_SELECTOR, value='#cookie')

click_cookie()
