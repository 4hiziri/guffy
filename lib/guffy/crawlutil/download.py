from bs4 import BeautifulSoup
import re
'''
this module offers some functions for crowling and scraping
'''

header = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":
    "gzip, deflate, sdch",
    "Accept-Language":
    "ja,en-US;q=0.8,en;q=0.6",
    "Cache-Control":
    "max-age=0"
}


def get_bsObj(url, session, header=header):
    '''
    get_bsObj accesses to url using header, and return BeautifulSoup object.
    this uses lxml to parse html.
    cannot parsing page which use javascript.
    '''

    req = session.get(url, headers=header)
    return BeautifulSoup(req.text, features="lxml")


# :TODO def get_page_include_javascript()


def find_all_urls(bsObj):
    '''
    find_all_urls extracts all urls from access_trg, and return its list.
    way to extract url is finding tag-a which has href and getting url.
    '''

    tag_a = bsObj.findAll("a")
    tag_a_has_link = filter(lambda x: 'href' in x.attrs, tag_a)
    row_urls_str = map(lambda x: x.attrs.get('href'), tag_a_has_link)
    return list(row_urls_str)


def abs_path(host, address):
    '''
    abs_path concatenate host and address.
    return suitable link which is host/address.
    '''
    from urllib.parse import urljoin
    return urljoin(host, address)


def search_urls(urls, regex_pattern):
    '''
    search_urls returns urls list which matches regex_pattern.    
    '''

    def filter_func(x):
        result = re.search(regex_pattern, x)
        return result is not None

    filtered = filter(filter_func, urls)
    return list(filtered)
