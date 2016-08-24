import unittest

from selenium import webdriver


class LaunchBrowser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="c:/Users/Gary/Desktop/Selenium/chromedriver")

    def testBBSportWebsite(self):
        self.driver.set_window_size(1024, 720)
        self.driver.get("https://www.bbc.co.uk/sport")
        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//nav//a[@class="primary-nav__link" and @href="/sport/football"]').click()
        print(self.driver.current_url)
        time.sleep(3)
        self.assertEquals(self.driver.current_url, "http://www.bbc.co.uk/sport/football")
        pass

    def tearDown(self):
        self.driver.save_screenshot(self.driver.session_id + 'screenshot.png')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
