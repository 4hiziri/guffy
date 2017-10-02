from __init__ import *
import unittest
from bs4 import BeautifulSoup

class TestCrawlUtil(unittest.TestCase):
    html = '''<!DOCTYPE html>
<html class="client-js ve-not-available" dir="ltr" lang="ja">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <title>web page for test</title>
    <a href='/index.php'>test link</a>
    <a href='this/is/test'></a>
  </head>
</html>
'''

    bsObj = BeautifulSoup(html, features="lxml")

    def test_find_all_urls(self):
        self.assertListEqual(find_all_urls(self.bsObj),
                             ['/index.php', 'this/is/test'])

    def test_abs_path(self):
        self.assertEqual(abs_path('http://www.example.com', '/index.php'),
                         'http://www.example.com/index.php')
        self.assertEqual(abs_path('http://www.example.com/under1/', 'under2.txt'),
                         'http://www.example.com/under1/under2.txt')

    def test_search_urls(self):
        self.assertListEqual(search_urls(['https://www.example.com/test.txt',
                                          'https://www.example.com/test/test.jpg',
                                          'https://www.example.com/test/test1.jpg',
                                          'https://www.example.com/test/test02.jpg'],
                                         r'.*test[0-9]+.jpg'),
                             ['https://www.example.com/test/test1.jpg',
                              'https://www.example.com/test/test02.jpg'])

if __name__ == '__main__':
    unittest.main()
