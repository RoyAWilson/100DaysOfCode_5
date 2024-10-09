'''
Scrape the events section from the
python.org landing page with selenium
into a dictionary
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

URL = r'https://www.python.org/'

driver.get(url=URL)

# Grab the named span:

event_times: str = driver.find_elements(
    By.CSS_SELECTOR, value='.event-widget time')
event_names: str = driver.find_elements(
    By.CSS_SELECTOR, value='.event-widget li a')
# for time in event_times:
#     print(time.text)
# for name in event_names:
#     print(name.text)

events: dict = {i: {event_times[i].text: event_names[i].text} for i in range(
    0, len(event_times))}
# tutor used a for loop instead of a dict comprehension.
print(events)
driver.close()
