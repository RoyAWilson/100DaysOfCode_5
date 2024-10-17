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
from protonmail import ProtonMail


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
time.sleep(40)

# Find Easy Apply jobs only:
# Have got it to work, at last! Can't see that anything different to what I did several times
# except I assigned the element to a variable then sent the click.  Hope it works still when come back
# in a while.
EA_Jobs = driver.find_element(By.XPATH, '//button[text()="Easy Apply"]')
EA_Jobs.click()
time.sleep(30)

# Grab some details of the first page of jobs to save or send to self:
cont = driver.find_element(
    By.CSS_SELECTOR, value='.scaffold-layout__list-container')
strong = cont.find_elements(by=By.TAG_NAME, value='strong')
titles: list = []
for title in strong:
    titles.append(title.text)
# print(titles)

# set up message text:
mess_text = f'The following jobs are available on easy apply today:\n'
for title in titles:
    mess_text += f'{title}\n'
mess_text += 'Check them out!'

# Send titles to self:
OUTMAIL = os.getenv('FROM_EMAIL')
PASSWORD = os.getenv('FROM_PASSWORD')
TO_ADDY = os.getenv('TO_EMAIL')

# set up email:
proton = ProtonMail()
proton.login(username=OUTMAIL, password=PASSWORD)

new_message = proton.create_message(
    recipients=[TO_ADDY],
    subject='New Jobs on Easy Apply Today!',
    body=mess_text
)
proton.send_message(new_message)
proton.save_session('session.pickle')
