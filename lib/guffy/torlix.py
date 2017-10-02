"""This is utlility for tor-thorw-scraping"""

# TODO: integration

import sys
import urllib
from bs4 import BeautifulSoup
import socks
import socket
from . import lix

# dummy-header
# If more correct one is found, Change this header immediately.

header = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Accept":
    """text/html,\
        application/xhtml+xml,\
        application/xml;q=0.9,\
        image/webp,\
        */*;q=0.8""",
    "Accept-Encoding":
    "gzip, deflate, sdch",
    "Accept-Language":
    "ja,en-US;q=0.8,en;q=0.6",
    "Cache-Control":
    "max-age=0"
}


def create_connection(address, timeout=None, source_address=None):
    "This creates tor-connection and Return Sock object."
    sock = socks.socksocket()
    sock.connect(address)
    return sock


def get_bsObj_over_tor(url):
    "This return bs object from url with tor"
    # proxy setting
    addr = "127.0.0.1"
    socks.setdefaultproxy(
        proxy_type=socks.SOCKS5, addr=addr, port=9150, rdns=True)

    socket.socket = socks.socksocket
    socket.create_connection = create_connection

    r = urllib.request.urlopen(url, timeout=1800)
    return BeautifulSoup(r.read(), features='lxml')


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        query = sys.argv[2]
        url = sys.argv[1]
        links = lix.link_extract(get_bsObj_over_tor(url), query)
        for link in links:
            print(link)
    else:
        print("torlix <url> <regex>")
