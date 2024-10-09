''''
Intro to selenium
selenium dox: https://selenium-python.readthedocs.io/
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up web driver

driver = webdriver.Firefox()

# Get a webpage:
# For chrome driver apparently have to set variable to
# #webdriver.ChromeOptions and variable.add.experimental_option('detach', True)
# To stop the instance of browser closing automatically on end of program.

driver.get(url='https://www.amazon.co.uk/Russell-Hobbs-Freestanding-Stainless-RH90AFF201SS/dp/B0CQ2KH398/ref=sr_1_11?crid=3QWBCKF544GS2&dib=eyJ2IjoiMSJ9.IfGeW5xLlPVAts1DEyFkbKVZsb-HTejVnL3elbg6jg4Vy81nwQ-BV8p7y16W2hObj_jcxY_kI707gH9DKnoUGzEsoGiL-tO8IL6fTi1RG5XPlD3d_wFtmC34q_HfjOlJ7XU4L-HycKh3NH1kHaIAsNqVc5EhAsTOyQkdqKSS-fG1haRYtTUSyniLwhsnWXWLVcVpJX-D9d1E-LyQCtdj1uJuI_rTiPtarS2uf1rCI24.fXO97NHfbjtRla_eZd4OPFOBuVfyq8Dfn4mAINdqlCw&dib_tag=se&keywords=fridge+freezer&qid=1728407678&sprefix=fridge+freezer%2Caps%2C185&sr=8-11')

# User selenium to get a eg. price for a product from an amazon page

# To close page when finished with it:
price_poundw: str = driver.find_element(
    By.CLASS_NAME, value='a-price-whole').text
prince_pence: str = driver.find_element(
    By.CLASS_NAME, value='a-price-fraction').text
print(f'The price of the Russell Hobbs free standing fridge freezer is £{
      price_poundw}.{prince_pence}')

driver.close()
# Also a method driver.quit() .close only closes only the tab quit closes browser completely
