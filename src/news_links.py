import os
import logging

from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.by import By

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'https://www.lankadeepa.lk/top_story/10/'


def firefox_example():
    firefox_options = firefox.options.Options()
    firefox_options.set_preference('browser.download.folderList', 2)
    firefox_options.set_preference(
        'browser.download.manager.showWhenStarting', False
    )
    firefox_options.set_preference('browser.download.dir', os.getcwd())
    firefox_options.set_preference(
        'browser.helperApps.neverAsk.saveToDisk', 'text/csv'
    )
    firefox_options.binary_location = '/opt/firefox/firefox'

    logging.info('Prepared firefox profile..')

    browser = webdriver.Firefox(options=firefox_options)
    logging.info('Initialized firefox browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    elems = browser.find_elements(By.CLASS_NAME,'news-title')
    print(len(elems))

    # for elem in elems:
        # print(elem.get_attribute("href"))


    browser.quit()



if __name__ == '__main__':
    firefox_example()
