import re
from . import scrapeutil as sutil
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
        
        has_attr = filter(lambda x: attr in x.attrs, page)
        return list(map(lambda x: x.attrs[attr], has_attr))
    
    
def extract_link(bsobj, class_=None, permit_other_host=False):
    """This extract links in href of a-tag.
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

# TODO: interval
        
if __name__ == '__main__':
    import argparse

    # argparse
    parser = argparse.ArgumentParser(description='link extractor')
    target_group = parser.add_mutually_exclusive_group()
    target_group.add_argument('-a',
                              '--all',
                              help='extract all link(support a-href and img-src now).',
                              action='store_true')
    target_group.add_argument('-i',
                              '--image',
                              help='extract from img tag.',
                              action='store_true')
    parser.add_argument('url',
                        help='URL that you want to extract links from.')
    parser.add_argument('-r',
                        '--regex',
                        help='Regex pattern for filtering links.',
                        default='.*')
    args = parser.parse_args()
    url = args.url
    regex = args.regex

    # main process
    bsObj = crawl.get_bsObj(url)

    if args.image:
        links = extract_img(bsObj)
    elif args.all:
        links = extract_img(bsObj)
        links += extract_link_by_query(bsObj, regex)
    else:
        links = extract_link_by_query(bsObj, regex)

    # need option
    links = sutil.regulate_url(url, links, True)

    # print links
    for link in links:
        print(link)
