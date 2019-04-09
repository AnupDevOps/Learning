'''
Created on Oct 18, 2018

@author: training_d2.03.07
'''
import unittest
from selenium import webdriver
from SeleniumDemo.LoginPageObject import LoginPageObjects


class Test(unittest.TestCase):


    def setUp(self):
        self.driver= webdriver.Chrome(r"C:\Selenium Advance\New_chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:8085/servlets/com.mercurytours.servlet.WelcomeServlet")
        self.driver.implicitly_wait(10)


    def tearDown(self):
        pass


    def testName(self):
        self.loginpgeobj=LoginPageObjects(self.driver)
        title=self.loginpgeobj.login("mercury", "mercury")
        self.assertEqual(title, "Find a Flight: Mercury Tours:", "Can't find title")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()