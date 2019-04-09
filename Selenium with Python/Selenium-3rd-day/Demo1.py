'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r"C:\Selenium Advance\New_chromedriver\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\Selenium Advance\FireFox\geckodriver.exe")
driver.maximize_window()
driver.get("http://localhost:8085/servlets/com.mercurytours.servlet.WelcomeServlet")
driver.implicitly_wait(10)
str1=driver.current_url  # Show to the current_url of the page
print(str1)
username=driver.find_element_by_name("userName") #it will search the element by name form the website
username.send_keys("mercury")
password=driver.find_element_by_name("password")
password.send_keys("mercury")
# signin=driver.find_element_by_name("login") #it will search the element by name form the website
signin=driver.find_element_by_xpath("//input[@name='login']") #it will search the element by xpath form the website
signin.click()
# driver.quit()
passengers=driver.find_element_by_name("passCount")
selectpassengers=Select(passengers)
selectpassengers.select_by_visible_text("3")

departingCity=driver.find_element_by_name("fromPort")
selectdepart=Select(departingCity)
selectdepart.select_by_visible_text("Frankfurt")

fromMonth=driver.find_element_by_name("fromMonth")
selectMonth=Select(fromMonth)
selectMonth.select_by_visible_text("May")

fromDay=driver.find_element_by_name("fromDay")
selectDay=Select(fromDay)
selectDay.select_by_visible_text("28")

signin=driver.find_element_by_name("findFlights")
signin.click()

# Another way of signin 
# driver.find_element_by_name("findFlights").click()

# driver.find_element_by_xpath("//a[text()='SIGN-OFF']").click()
#Another Way to SING-OFF
singout= driver.find_element_by_link_text("SIGN-OFF")
# Check the text of the button or link
stringtextforSignout=singout.text
singout.click()
print("The text is :", stringtextforSignout)
if stringtextforSignout == 'SIGN-OFF':
    print("Correct")
else:
    print("Incorrect")
driver.quit()
