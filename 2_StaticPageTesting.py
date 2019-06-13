from selenium import webdriver
from selenium.webdriver.common.keys import Keys
ch_browser=webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver")
ch_browser.get("file:///C:/Users/hp/Desktop/Programs/Selenium/test.html")
ch_browser.find_element_by_id("123").send_keys("rpaulpj@gmail.com")
ch_browser.find_element_by_id("456").send_keys("p@123")
ch_browser.find_element_by_name("q").click()

