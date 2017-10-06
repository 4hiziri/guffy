import re
from . import crawlutil as crawl

'''
This is link extractor, I call it lix.
lix will download page form URL and extract href link from that page.
After extraction, print links to stdout.
'''


def extract_element(bs, tag, attr, class_=None):
    "This extract attribute of tag. It can filter by class"
    if class_ is None:
        page = bs.find_all(tag)
    else:
        page = bs.find_all(tag, class_=class_)

    return list(map(lambda x: x.attrs[attr],
                    filter(lambda x: attr in x.attrs, page)))


def extract_link(bsobj, class_=None, permit_other_host=False):
    """This extract links in href of a-tag.
    NOT IMPLEMENT!
    If permit_other_host is True,
    this returns links including extern host's address"""
    # get all links in page.
    return extract_element(bsobj, 'a', 'href', class_=class_)


def extract_link_by_query(bsObj, query):
    """This extract link from `bsObj` and filter them by query"""

    return crawl.search_urls(crawl.find_all_urls(bsObj), re.compile(query))


def extract_img(bsobj):
    "This extract value of src in img-tag"
    return extract_element(bsobj, 'img', 'src')

# TODO: extract_img_by_query
