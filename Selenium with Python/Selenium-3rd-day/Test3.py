'''
Created on Oct 17, 2018

@author: training_d2.03.07
'''
import unittest
from selenium import webdriver
# from selenium.webdriver.support.select import Select


class Test1(unittest.TestCase):


    def setUp(self):
        print("Pre Conditions")
        self.driver= webdriver.Chrome(r"C:\Selenium Advance\New_chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:8085/servlets/com.mercurytours.servlet.WelcomeServlet")
        self.driver.implicitly_wait(10)


    def tearDown(self):
        print("Post conditions")
        self.driver.quit()


    def testLogin(self):
        print("Login test case")
        username=self.driver.find_element_by_name("userName") #it will search the element by name form the website
        username.send_keys("mercury")
        password=self.driver.find_element_by_name("password")
        password.send_keys("mercury")
        # signin=driver.find_element_by_name("login") #it will search the element by name form the website
        signin=self.driver.find_element_by_xpath("//input[@name='login']") #it will search the element by xpath form the website
        signin.click()
        self.assertEqual(self.driver.title, "Find a Flight: Mercury Tours:", "Find Flight is not there")
        

    def testRegister(self):
        print("Register Test case")
        self.driver.find_element_by_xpath("//a[text()='REGISTER']").click()
        username=self.driver.find_element_by_name("userName") #it will search the element by name form the website
        username.send_keys("mercury1")
        password=self.driver.find_element_by_name("password")
        password.send_keys("mercury1")
        cpassword=self.driver.find_element_by_name("confirmPassword")
        cpassword.send_keys("mercury1")
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()