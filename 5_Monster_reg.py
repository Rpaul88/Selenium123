import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver")
driver.get("https://www.monsterindia.com/seeker/registration")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//*[@class='box tc']").click()
driver.find_element_by_name("fullname").send_keys("Rajesh")
driver.find_element_by_name("email").send_keys("abc@123")
driver.find_element_by_xpath("//*[@class='input pr30']").send_keys("123456")

driver.find_element_by_xpath("//div[contains(@class,'multiselect modal-ref-class multiBox')]").click()
driver.find_element_by_xpath("//input[contains(@class,'multiselect__input')]").send_keys("Thr")
time.sleep(2)
driver.find_element_by_xpath("//input[contains(@class,'multiselect__input')]").send_keys(Keys.ENTER)

driver.find_element_by_name("Mobile Number").send_keys("9846875466")
driver.find_element_by_id("file-upload").send_keys("C:/Users/Guest User/Desktop/RAJESH/RAJESH_Resume April 2019.pdf")
