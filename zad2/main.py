import time

from selenium import webdriver
from selenium.webdriver import Keys, DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging
import unittest


class MainUnitTests(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = logging.getLogger('simple_example')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        s = Service("C:\\Users\\Krystian\\PycharmProjects\\TAU_Rozwiazania\\zad2\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    def test_Userbenchmark_compare(self):
        self.logger.info("Entering Userbenchmark")
        self.driver.get("https://gpu.userbenchmark.com")

        self.logger.info("Get all graphics card links on main page")
        temp = self.driver.find_elements(By.CLASS_NAME, "nodec")

        found = False
        for a in temp:
            if "RTX 3060-Ti" in a.accessible_name:
                a.click()
                self.logger.info("Go to RTX 3060-Ti")
                break

        time.sleep(2)

        temp = self.driver.find_element(By.CLASS_NAME, "row.hovertarget")
        temp = temp.find_elements(By.XPATH, ".//*")
        for a in temp:
            if "RTX 3070" in a.accessible_name:
                a.click()
                self.logger.info("Picking RTX 3070 as comparison")
                found = True
                break

        if not found:
            self.fail("Phone not found!")

        self.logger.info("Getting GameEFps score")
        temp = self.driver.find_element(By.CLASS_NAME, "boxthumb.comp-headerwrapper.comp-headerwrapper-dropdown.dropdown")
        temp = temp.find_element(By.CLASS_NAME, "innercolright")
        self.assertEqual(temp.text, "+7%")


    def test_Ceneo_favourite(self):
        self.logger.info('Entering Ceneo')
        self.driver.get('https://www.ceneo.pl')
        temp = self.driver.find_element(By.NAME, 'search-query')
        self.logger.info('Searching for: Apple iPhone 12 64GB Czarny Black')
        temp.send_keys("Apple iPhone 12 64GB Czarny Black")
        temp.send_keys(Keys.ENTER)

        temp = self.driver.find_elements(By.CLASS_NAME,
                                         "cat-prod-row.js_category-list-item.js_clickHashData.js_man-track-event")
        found = False
        for div in temp:
            if "Apple iPhone 12 64GB Czarny Black" in div.text:
                self.logger.info('Found phone')
                div.click()
                found = True
                break

        if not found:
            self.fail("Phone not found!")

        time.sleep(2)
        temp = self.driver.find_element(By.CLASS_NAME,
                            "add-to-favorite.js_no-conv.js_wishlist-toggle.js_sa-wishlist-item.js_gtm_wishlist-toggle")
        temp.click()
        self.logger.info("Added to favourite")
        temp = self.driver.find_element(By.CLASS_NAME, "header__logo__link")
        temp.click()
        self.logger.info("Going to main page")

        self.logger.info('Searching for: Xiaomi Mi Note 10 Pro 8/256GB Biały')
        temp = self.driver.find_element(By.NAME, 'search-query')
        temp.send_keys("Xiaomi Mi Note 10 Pro 8/256GB Biały")
        temp.send_keys(Keys.ENTER)

        temp = self.driver.find_elements(By.CLASS_NAME,
                                         "cat-prod-row.js_category-list-item.js_clickHashData.js_man-track-event")
        found = False
        for div in temp:
            if "Xiaomi Mi 10T Pro 5G 8/256GB Czarny" in div.text:
                self.logger.info('Found phone')
                div.click()
                found = True
                break

        if not found:
            self.fail("Phone not found!")

        time.sleep(2)
        temp = self.driver.find_element(By.CLASS_NAME,
                                        "add-to-favorite.js_no-conv.js_wishlist-toggle.js_sa-wishlist-item.js_gtm_wishlist-toggle")
        temp.click()
        self.logger.info("Added to favourite")

        self.driver.get('https://www.ceneo.pl')
        self.logger.info("Going to main page")

        temp = self.driver.find_element(By.CLASS_NAME, "header__user__favourites")
        temp.click()

        temp = self.driver.find_element(By.ID, "clipboard")
        temp.click()

        temp = temp.find_elements(By.TAG_NAME, "img")
        self.logger.info("Get active favorite objects")
        self.assertEqual(2, len(temp)/2)


if __name__ == '__main__':
    unittest.main()