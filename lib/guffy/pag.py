'''
Need PhantomJS
# sudo apt-get install phantomjs
fetch javascript page.

TODO: integration
'''

from bs4 import BeautifulSoup
from selenium import webdriver
from . import crawlutil as crawl

header = crawl.header


def get_bsObj_JS(url, span=3):
    """This function gets BeautifulSoup Object of page with javascript from URL,
span is needed for execution of javascript."""

    import time

    driver = webdriver.PhantomJS(executable_path='/usr/bin/PhantomJS')
    driver.get(url)
    time.sleep(span)  # execution time for javascript
    obj = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    return obj
