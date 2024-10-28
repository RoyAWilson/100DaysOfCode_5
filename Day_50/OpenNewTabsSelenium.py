'''
Day 50 of 100DaysOfCode Udemy Course

Didin't like the Tinder swiper project given by the tutor so decided to
replicate the new stuff in that project - navigating between tabs and closing them.
Took a pretty big amount of research in the documentation and other resources but got there.
'''

from time import sleep
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://www.google.com/search?q=python&sca_esv=977fe9b89071f032&source=hp&ei=zr0fZ-DjA42ChbIP2fqYUQ&iflsig=AL9hbdgAAAAAZx_L3sSQLrEfJmXhzpkMNIQX0_1Bh_st&ved=0ahUKEwjggsavwbGJAxUNQUEAHVk9JgoQ4dUDCBM&oq=python&gs_lp=Egdnd3Mtd2l6IgZweXRob25IAFAAWABwAHgAkAEAmAEAoAEAqgEAuAEMyAEAmAIAoAIAmAMAkgcAoAcA&sclient=gws-wiz')
sleep(15)
first_result = ui.WebDriverWait(browser, 15).until(
    lambda browser: browser.find_element(by=By.CLASS_NAME, value='yuRUbf'))
first_link = first_result.find_element(by=By.TAG_NAME, value='a')

# save the window opener (Current Window.  Do not mistake with tab name.  Not the same)

main_window = browser.current_window_handle

# Open the link in a new tab by sending key strokes to the eleemnt
first_link.send_keys(Keys.CONTROL + Keys.RETURN)
browser.switch_to.window(browser.window_handles[1])
# Do whatever you have to do
sleep(10)
browser.close()
browser.switch_to.window(browser.window_handles[0])
# Double check that the first page remains open after closing out the new tab.
first_link.click()
sleep(60)
browser.close()
