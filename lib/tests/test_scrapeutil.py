import unittest
from guffy import scrapeutil as sutil

test_dir1 = "test-dir"
test_dir2 = "exists-dir"


class TestScarpeUtil(unittest.TestCase):
    def test_mkdir_ifnotexists(self):
        import os
        os.makedirs(test_dir2)

        sutil.mkdir_ifnotexists(test_dir1)
        self.assertTrue(os.path.exists(test_dir1))
        # How to test that this does not raise exception?
        sutil.mkdir_ifnotexists(test_dir2)

        os.removedirs(test_dir1)
        os.removedirs(test_dir2)

    def test_isfile(self):
        url_t = 'http://www.example.com/test.pdf'
        url_f = 'http://www.example.com/test2/'
        self.assertTrue(sutil.isfile(url_t))
        self.assertFalse(sutil.isfile(url_f))

    def test_get_host(self):
        url = 'http://www.example.com/test/test.txt'
        self.assertEqual(sutil.get_host(url), 'www.example.com')

    def test_get_path(self):
        url = 'http://www.example.com/test/test.txt'
        self.assertEqual(sutil.get_path(url), '/test/test.txt')

    def test_remove_dif_host(self):
        host = 'www.example.com'
        urls = [
            'https://www.example.com/test1', 'https://www.example.com/test2',
            'http://www.example.com/test1', 'https://www.example2.com/test1'
        ]
        correct = [
            'https://www.example.com/test1', 'https://www.example.com/test2',
            'http://www.example.com/test1'
        ]

        self.assertEqual(sutil.remove_dif_host(host, urls), correct)

    def test_get_filename(self):
        url = 'http://www.example.com/test/test.txt'
        self.assertEqual(sutil.get_filename(url), 'test.txt')

    def test_regulate_url(self):
        url = 'https://www.example.com/test/index.php'
        urls = [
            '/test/test.txt', 'send/line/', 'http://www.example2.com/index.php'
        ]
        correct_f = [
            'https://www.example.com/test/test.txt',
            'https://www.example.com/test/send/line/'
        ]
        correct_t = correct_f + ['http://www.example2.com/index.php']

        self.assertEqual(sutil.regulate_url(url, urls, False), correct_f)
        self.assertEqual(sutil.regulate_url(url, urls, True), correct_t)


if __name__ == '__main__':
    unittest.main()
