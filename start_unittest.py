import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create test case
class PythonOrgSearch(unittest.TestCase):
    #set up usually starts with what browser to use
    def setUp(self):
        self.driver = webdriver.Firefox()

    #test case method/steps. Test case method should always start with the word test
    def test_search_in_python_org(self):
        #should create a local reference to the driver object
        driver = self.driver
        driver.get("http://www.python.org")
        #syntax of assert is different compared with non-unittest code
        self.assertIn("Python",driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    #will be executed after test method
    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()


