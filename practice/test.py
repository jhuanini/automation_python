import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#create test case
class PythonOrgSearch(unittest.TestCase):
    #set up usually starts with what browser to use
    def setUp(self):
        self.driver = webdriver.Chrome()

    #test case method/steps. Test case method should always start with the word test
    def test_search_in_python_org(self):
        #should create a local reference to the driver object
        driver = self.driver
        driver.get("http://www.facebook.com")
        #self.driver.find_element_by_id("email")
        assert "facebook" in self.driver.title


    if __name__ == '__main__':
        unittest.main()


