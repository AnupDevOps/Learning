'''
Created on Oct 17, 2018

@author: training_d2.03.07
'''
# Action Demo Control your Mouse action on the website
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Actionchains(drivers) is the class which we used in python for the selenium

driver1 = webdriver.Chrome(r"C:\Selenium Advance\New_chromedriver\chromedriver_win32\chromedriver.exe")
driver1.maximize_window()
driver1.get("http://jqueryui.com/resources/demos/droppable/default.html")
driver1.implicitly_wait(5)

src= driver1.find_element_by_id("draggable")
dest= driver1.find_element_by_id("droppable")
ActionChains(driver1).drag_and_drop(src, dest).perform()