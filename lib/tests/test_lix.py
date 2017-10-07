import unittest
from guffy import lix


class TestLix(unittest.TestCase):
    from bs4 import BeautifulSoup
    html = '''<!DOCTYPE html>
<html class="client-js ve-not-available" dir="ltr" lang="ja">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <title>web page for test</title>
    <a href='/index.php'>test link</a>
    <a href='this/is/test'></a>
    <img src='img/testsource'>
  </head>
</html>
'''

    bsObj = BeautifulSoup(html, "lxml")

    def test_extract_element(self):
        self.assertListEqual(
            lix.extract_element(self.bsObj, 'a', 'href'),
            ['/index.php', 'this/is/test'])
        self.assertListEqual(
            lix.extract_element(self.bsObj, 'img', 'src'), ['img/testsource'])

    def test_extract_link(self):
        self.assertListEqual(
            lix.extract_element(self.bsObj, 'a', 'href'),
            lix.extract_link(self.bsObj))

    def test_extract_link_by_query(self):
        self.assertListEqual(
            lix.extract_link_by_query(self.bsObj, '.*\.php'), ['/index.php'])

    def test_extract_img(self):
        self.assertListEqual(lix.extract_img(self.bsObj), ['img/testsource'])


if __name__ == '__main__':
    unittest.main()
