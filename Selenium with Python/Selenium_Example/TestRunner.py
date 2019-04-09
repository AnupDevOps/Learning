'''
Created on Oct 17, 2018

@author: training_d2.03.07
'''
import unittest
from SeleniumDemo.UnitTestFrameWork_N import Test
from SeleniumDemo.Test3 import Test1
import HtmlTestRunner
from unittest import runner

loader= unittest.TestLoader()
suite1= unittest.TestSuite()

suite1.addTest(loader.loadTestsFromTestCase(Test))
suite1.addTest(loader.loadTestsFromTestCase(Test1))

# runner= unittest.TextTestRunner()
# runner.run(suite1)

runner= HtmlTestRunner.HTMLTestRunner(output='Test-reports',report_title='TestCaseReport')
runner.run(suite1)