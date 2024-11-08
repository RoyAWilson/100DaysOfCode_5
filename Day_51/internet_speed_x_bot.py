'''
Class to handle tweeting internet speeds up and down
'''
import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from dotenv import load_dotenv


class InternetSpeedXBot():

    '''
    To handle setting up the selenium driver
    And tweeting the results of the test.
    '''

    load_dotenv()

    PROMISED_UP = 150
    PROMISED_DOWN = 10
    X_EMAIL: str | None = os.getenv('ACCOUNT_NAME')
    X_PASS: str | None = os.getenv('PASSWORD')
    PHONE: str | None = os.getenv('PHONE')

    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.up = 0
        self.down = 0
        self.login: str | None = os.getenv('ACCOUNT_NAME')
        self.tweet_text = ''

    def get_internet_speed(self) -> None:
        '''
        Get the Internet Upload and Download Speeds from site
        '''
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(
            by=By.ID, value='onetrust-accept-btn-handler').click()
        sleep(15)
        self.driver.find_element(by=By.CLASS_NAME, value='start-text').click()
        sleep(50)
        self.down: str = self.driver.find_elements(
            by=By.CLASS_NAME, value='result-data-large')[0].text
        self.up: str = self.driver.find_elements(
            by=By.CLASS_NAME, value='result-data-large')[1].text
        # print(f'Your download speed is {
        #       self.down} and you upload speed is {self.up}')
        self.tweet_text: str = f'I am getting {
            self.down} download speeds and {self.up} upload speeds on BT.'

    def tweet_at_provider(self) -> None:
        '''
        Tweet the speeds
        '''
        self.driver.get('https://x.com/i/flow/login')
        self.driver.maximize_window()
        sleep(10)
        self.driver.find_element(
            by=By.TAG_NAME, value='input').send_keys(self.X_EMAIL, Keys.ENTER)
        sleep(15)
        self.driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(
            self.X_PASS, Keys.ENTER)
        sleep(25)
        tweet: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, 'div[aria-label="Post text"]')
        tweet.click()
        sleep(15)
        tweet.send_keys(self.tweet_text)
        ActionChains(self.driver).key_down(Keys.CONTROL).key_down(
            Keys.ENTER).key_up(Keys.CONTROL).key_up(Keys.ENTER).perform()
        sleep(60)
        self.driver.close()
