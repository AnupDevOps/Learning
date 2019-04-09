'''
Created on Oct 18, 2018

@author: training_d2.03.07
'''
import unittest
from selenium.webdriver.common.by import By
from SeleniumDemo.Demo1 import password, driver
from test.test_robotparser import PasswordProtectedSiteTestCase
from test.test_statistics import sign


class LoginPageObjects(object):
    user_name=(By.NAME, "userName")
    pass_word=(By.NAME, "password")
    sign_in=(By.NAME, "login")
    
    def login(self,user,pwd):
        username=self.driver.find_element(*self.user_name)
        username.send_keys(user)
        password=self.driver.find_element(*LoginPageObjects.pass_word)
        password.send_keys(pwd)
        signin= self.driver.find_element(*LoginPageObjects.sign_in)
        signin.click()
        return self.driver.title

    def __init__(self,driver):
        self.driver=driver
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()