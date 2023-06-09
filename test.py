import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        self.browser.get("https://www.instagram.com/")
        self.assertIn('Instagram', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
