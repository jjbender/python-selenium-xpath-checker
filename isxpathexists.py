import logging
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import InvalidSelectorException


def xpathCheckInput():
  global url
  url = input('insert url: ')
  global xpath
  xpath = input('insert xpath: ')

def driverPreferences():
    firefox_profile.set_preference('intl.accept_languages', 'ru'); #might be en
    #firefox_profile.set_preference('permissions.default.image', 2)
    #firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    #firefox_profile.set_preference('general.useragent.override', 'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36')

def printOutput(output):
    global element_text
    element_text = output.text
    global element_tag_name
    element_tag_name = output.tag_name
    global element_parent
    element_parent = output.parent
    global element_location
    element_location = output.location
    global element_size
    element_size = output.size
"""

url_links = driver.find_elements_by_tag_name("a")
url_fields = driver.find_elements_by_tag_name("input")

def honeypotSearch(url_links,url_fields):
    #for link in url_links:
    #    if not link.is_displayed():
    #        logging.info("The link ", link.get_attribute("href")," is a trap")
    for field in url_fields:
        if not field.is_displayed():
            logging.info("Do not change value of " + field.get_attribute("name"))
"""

logging.basicConfig(level=logging.DEBUG)

xpathCheckInput()

firefox_profile = webdriver.FirefoxProfile()
driverPreferences()
driver = webdriver.Firefox(firefox_profile = firefox_profile)

start_time = time.time()

try:
    driver.get(url)
except (InvalidArgumentException):
    url = input('wrong url, insert correct url: ')
    start_time = time.time()
    driver.get(url)

end_time = time.time()
logging.info(url,'url opened')
logging.debug(start_time)
logging.debug(end_time)
average_load = round((end_time-start_time),3)
print('load time is',average_load)

while True:
    try:
        output = driver.find_element_by_xpath(xpath)
    except(InvalidSelectorException):
        logging.info('InvalidSelectorException')
    printOutput(output)
    logging.info(element_text)
    logging.info(element_tag_name)
    logging.info(element_location)
    logging.info(element_parent)
    logging.info(element_size)
    with open('xpath_log.csv', mode='a+', encoding='utf-8') as xpath_log:
        fieldnames = ['url', 'xpath','recommended webDriverWait','element_text','element_tag_name','element_parent','element_size','element_location']#,'detected Honeypots']
        writer = csv.DictWriter(xpath_log, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'url' : url, 'xpath' : xpath, 'recommended webDriverWait' : average_load, 'element_text': element_text, 'element_tag_name': element_tag_name, 'element_parent' : element_parent, 'element_size' : element_size, 'element_location' : element_location})
    if input('Type \'Y\' to try another xpath?') == 'Y':
        xpath = input('Type another xpath')
        True
    else:
        break


driver.close()
driver.quit()
logging.debug('End of Program')
