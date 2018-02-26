import unittest
from selenium import webdriver
#waits for the page to load
from selenium.webdriver.support.ui import WebDriverWait
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

    #test case method
    def test_login(self):
        driver = self.driver

        #declare variables
        fbusername = 'jhuanini'
        fbpw = 'mahalpabanyako'
        fbusernameid = 'email'
        fbpwid = 'pass'
        loginbuttonxpath = '//*[@id="u_0_2"]'
        fblogocssselector = 'span._2md'

        fbusernameelement = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id(fbusernameid))
        fbpwelement = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_id(fbpwid))
        loginbuttonelement = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(loginbuttonxpath))
        fbusernameelement.clear()
        fbusernameelement.send_keys(fbusername)
        fbpwelement.clear()
        fbpwelement.send_keys(fbpw)
        loginbuttonelement.click()
        fblogoclassnameelement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_css_selector(fblogocssselector))
        fblogoclassnameelement.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()