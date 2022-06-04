import os
import logging

from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.by import By

logging.getLogger().setLevel(logging.INFO)

BASE_URL_NEWS = 'https://www.lankadeepa.lk/top_story/10/'
BASE_URL_KNOWLEDGE = 'https://www.lankadeepa.lk/encyclopedia/17'
BASE_URL_FOREIGN = 'https://www.lankadeepa.lk/world_news/14'
BASE_URL_FEATURED = 'https://www.lankadeepa.lk/sunday/rasawitha/57'#didnt work
BASE_URL_CELEBRITY = 'https://www.saaravita.lk/bollyhollywood/105'#didnt work
BASE_URL_TRAVEL = 'https://www.saaravita.lk/travel/110'#didnt work


ARTCLE_TYPE_KNOWLEDGE = 0
ARTCLE_TYPE_FOREIGN = 1
ARTCLE_TYPE_FEATURED = 2
ARTCLE_TYPE_CELEBRITY = 3
ARTCLE_TYPE_TRAVEL = 4
ARTCLE_TYPE_NEWS = 5


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

    browser.get(BASE_URL_NEWS)
    logging.info('Accessed %s ..', BASE_URL_NEWS)

    logging.info('Page title: %s', browser.title)

    elems = browser.find_elements(By.CLASS_NAME,'news-title')

    for elem in elems:
        print(elem.get_attribute("href"))


    browser.quit()



if __name__ == '__main__':
    firefox_example()
