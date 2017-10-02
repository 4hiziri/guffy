import os
import requests
from . import crawlutil as crawl
from . import scrapeutil as sutil
from . import torlix


def download_req(url):
    return requests.get(url, headers=header).content


def download_tor(url, query, store):
    bsobj = torlix.get_bsObj_over_tor(url)
    
    if len(bsobj.contents) != 0:
        return bsobj.contents[0].text
    else:
        return None


if __name__ == '__main__':
    import sys
    import argparse

    # argparse
    parser = argparse.ArgumentParser(description="Downloader")
    parser.add_argument('url',
                        help='URL that you want to download.')
    parser.add_argument('dir',
                        help='Directory that you want to store file.')
    parser.add_argument('-p',
                        '--prefix',
                        help='Prefix for filename. -p pref means data is stored as pref<filename>.',
                        default='')

    args = parser.parse_args()

    # main part
    data = download_req(args.url)
    prefix = args.prefix
    filename = prefix + sutil.get_filename(sys.argv[1])
    dirname = args.dir

    if not os.path.exists(dirname):
        sutil.mkdir_ifnotexists('./' + dirname + "/")

    path = dirname + "/" + filename
    if not os.path.exists(path):
        sutil.write2file(path, data, 'wb')
