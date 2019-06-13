from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ch_browser=webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver")

ch_browser.get("http://google.com")
ch_browser.find_element_by_name("q").send_keys("testing")
ch_browser.find_element_by_name("q").send_keys(Keys.ENTER)