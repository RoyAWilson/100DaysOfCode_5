'''
Class to use selenium to login to Instagram,
navigate to a followed user
and follow that users followers.
Thinking that I will actually only follow a few of the user's followers.
'''

import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv

load_dotenv()


class InstaFollower():
    """_summary_
    To open open browser navigate to instagram
    then to navigate to a followed account and
    follow several of the account's followers.
    """

    def __init__(self) -> None:

        self.user: str | None = os.getenv('EMAIL')
        self.password: str | None = os.getenv('PASS')
        self.driver = webdriver.Firefox()
        self.url = r'https://www.instagram.com/'

    def login(self):
        """_summary_
        Login to Insta and navigate to a followed page using selenium.
        User Name and Password should be provided in a .env file.
        """
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
        self.driver.find_element(
            By.XPATH, "//button[text()='Decline optional cookies']").click()
        self.driver.maximize_window()
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[aria-label="Phone number, username or email address"]').send_keys(self.user)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[aria-label="Password"]').send_keys(self.password)
        sleep(30)
        self.driver.find_element(
            By.XPATH, '//button[@type="submit"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(
            By.XPATH, '//div[text()="Not now"]').click()
        sleep(15)
        self.driver.get('https://www.instagram.com/terrypratchettbooks')
        sleep(30)

    def find_followers(self) -> None:
        """
        _summary_
        To open followers frame and click on follow buttons of several of the
        accounts followers.
        """
        self.driver.find_element(
            By.XPATH, "//a[contains(@href, '/followers')]").click()
        sleep(5)
        follow_buts: ec.List[WebElement] = self.driver.find_elements(
            By.TAG_NAME, 'button')
        sleep(5)
        # NEED TO CHECK BELOW, IF WAS CASE OF NOT WAITING LONG ENOUGH FOR THE BUTTON TO BE CLICKABLE.
        # for but in follow_buts:
        #     but.click()
        #     sleep(5)

    def follow(self) -> None:
        pass
