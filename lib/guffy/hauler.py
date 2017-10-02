
import requests
from . import crawlutil as crawl
from . import torlix


def download_req(url):
    return requests.get(url, headers=crawl.header).content


def download_tor(url, query, store):
    bsobj = torlix.get_bsObj_over_tor(url)

    if len(bsobj.contents) != 0:
        return bsobj.contents[0].text
    else:
        return None
