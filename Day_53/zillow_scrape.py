"""_summary_
grab given website and grab prices, addresses and links
add to a google form and then use that to produce a google sheet.
"""

import os
from time import sleep
from dotenv import load_dotenv
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup, ResultSet

load_dotenv()

SF_URL = r'https://appbrewery.github.io/Zillow-Clone/'
FORM_URL = os.getenv('FORM_URL')


class ScrapeSF():
    """_summary_
    To Scrape the given webpage and add scraped details to lists
    of addresses, prices and  URLs
    """

    def __init__(self) -> None:
        self.rqst: requests.Response = requests.get(url=SF_URL, timeout=25)
        self.soup = None
        self.all_addresses: ResultSet
        self.address_list = []
        self.rep_address = ''
        self.all_prices = ''
        self.price = ''
        self.price_list = []
        self.link = ''
        self.all_links = ''
        self.link_list = []

    def scrape_urls(self) -> None:
        """_summary_
        Grab the required data with beautiful soup and produce lists containing the data
        to pass to next method.
        """
        self.soup = BeautifulSoup(self.rqst.content, 'html5lib')
        self.all_addresses: ResultSet = self.soup.findAll('address')

        # Assign addresses to var self.rep_address and strip addresses and remove | symbol

        for i in range(0, len(self.all_addresses)):
            self.rep_address = self.all_addresses[i].getText(
            ).strip().replace('|', '')
            self.address_list.append(self.rep_address)

        # Grab prices and assign to price list:
        self.all_prices = self.soup.find_all(
            'span', attrs={'class': 'PropertyCardWrapper__StyledPriceLine'})
        for j in range(0, len(self.all_prices)):
            self.price = self.all_prices[j].getText().strip().replace(
                '+', '').replace('/', '').replace('mo', '').replace(' *', '').split(' ')[0]
            self.price_list.append(self.price)

        # Grab Links:
        self.all_links = self.soup.find_all(
            'a', attrs={'class': 'StyledPropertyCardDataArea-anchor'})
        for l in range(0, len(self.all_links)):
            self.link = self.all_links[l]['href']
            self.link_list.append(self.link)

    def display_results(self):
        """_summary_
        Simply prints out the contents of the lists one by one, should it be necessary
        """
        for iter in range(0, len(self.address_list)):
            print(f'Address: {self.address_list[iter]}, Rent per month {
                  self.price_list[iter]}\nURL {self.link_list[iter]}\n\n')

    def Write_to_form(self):
        pass
