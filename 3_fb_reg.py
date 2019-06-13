from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ch_browser=webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver")
ch_browser.get("https://www.facebook.com")

ch_browser.find_element_by_id("u_0_l").send_keys("Stephen")
ch_browser.find_element_by_id("u_0_n").send_keys("Poovathingal")
ch_browser.find_element_by_id("u_0_q").send_keys("rpaulpj88@gmail.com")
ch_browser.find_element_by_id("u_0_t").send_keys("rpaulpj88@gmail.com")
ch_browser.find_element_by_id("u_0_x").send_keys("R6j35h@123")
ch_browser.find_element_by_id("day").send_keys("2")
ch_browser.find_element_by_id("u_0_6").click()
ch_browser.find_element_by_id("u_0_15").send_keys(Keys.ENTER)


#ch_browser.find_elements_by_xpath("//*[@id='u_0_j")
