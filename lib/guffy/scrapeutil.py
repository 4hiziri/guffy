import os
import urllib


def write2file(name, data, mode='w'):
    try:
        with open(name, mode) as f:
            f.write(data)
    except IsADirectoryError as e:
        write2file(name + '.txt', data, mode)


def mkdir_ifnotexists(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def isfile(path):
    root, ext = os.path.splitext(path)
    return ext is not ''


def get_host(url):
    return urllib.parse.urlparse(url).netloc


def get_path(url):
    return urllib.parse.urlparse(url).path


def remove_dif_host(host, urls):
    return list(filter(lambda x: get_host(x) == host, urls))


# TODO change
def get_filename(url, dirname=None):
    from urllib.parse import urlparse
    
    return os.path.basename(urlparse(url).path)


def urljoin_all(url, lst):
    return list(map(lambda x: urllib.parse.urljoin(url, x), lst))


def regulate_url(url, list_url, permit_other_host):
    # abs path
    links = urljoin_all(url, list_url)

    if permit_other_host:
        return links
    else:  # filtering extern host.
        return remove_dif_host(get_host(url), links)
