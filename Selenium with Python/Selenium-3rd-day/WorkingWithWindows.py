'''
Created on Oct 18, 2018

@author: training_d2.03.07
'''
import unittest
from selenium import webdriver
from pip._internal.utils.outdated import SELFCHECK_DATE_FMT



class Test(unittest.TestCase):


    def setUp(self):
        print("Pre Conditions")
        self.driver= webdriver.Chrome(r"C:\Selenium Advance\New_chromedriver\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://www.google.com")
        self.driver.implicitly_wait(10)


    def tearDown(self):
        print("Post conditions")
        self.driver.quit()


    def testName(self):
        print("Test in normal way")
        #self.driver.find_element_by_xpath("//button[@title='Close']").click()
    
    def testFrames(self):
        self.driver.switch_to_frame(0)
        self.driver.find_element_by_xpath("//button[@title='Close']").click()
        self.driver.switch_to_default_content()
        
        
        
        
        # Working with Windows
        windows=self.driver.window_handles
        for windowid in windows:
            self.driver.switch_to_window(windowid)
                
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()