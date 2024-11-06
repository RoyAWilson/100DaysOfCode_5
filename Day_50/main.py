'''
For day 50 project:
Sign in to good reads and
Find a list of books
Grab the title, author and link to the review page
Create it into a dataframe and export as an excel file.
'''

from time import sleep
import os
from dotenv import load_dotenv
import pandas as pd
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys

load_dotenv()

browser = webdriver.Firefox()

URL = r'https://www.goodreads.com/'
USER = os.getenv('USER')
PW = os.getenv('PWORD')

book_dict = {}
db = []

browser.get(URL)
sleep(5)
# Sign in
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

# Navigate to a list

browser.find_element(
    by=By.CLASS_NAME, value='primaryNavMenu__trigger').click()
sleep(5)
browser.find_element(by=By.LINK_TEXT, value='Lists').click()
sleep(15)
browser.find_element(by=By.LINK_TEXT, value='Historical Fiction').click()
sleep(15)
browser.find_element(by=By.LINK_TEXT, value='Best Middle Ages Books').click()
sleep(15)

# Scrape the required details

authors = browser.find_elements(by=By.CLASS_NAME, value='authorName')
titles = browser.find_elements(by=By.CLASS_NAME, value='bookTitle')
links = browser.find_elements(by=By.CSS_SELECTOR, value='.bookTitle')
values = [author.text for author in authors]
titles = [title.text for title in titles if title.text != '']
links = [link.get_attribute('href') for link in links]
# remove duplicates that have been added to the list for some reason
new_links = []
for link in links:
    if link not in new_links:
        new_links.append(link)
# Remove extras that get added to the end of the list
# # don't know where from as they don't come up when searching the page.
new_links = new_links[0:100]

# Close the session

browser.close()

# Create a list of dictionaries to form the dataframe from

for i in range(0, len(titles)):
    book_dict = {
        'Title': titles[i],
        'Author': values[i],
        'Link': new_links[i]
    }
    db.append(book_dict)
book_df = pd.DataFrame(db)

# Export to Excel file

book_df.to_excel('books.xlsx', index=False, header=True)
