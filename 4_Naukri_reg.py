from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

ch_browser = webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver")
ch_browser.get("https://my.naukri.com/account/createaccount")

ch_browser.implicitly_wait(10)
ch_browser.find_element_by_xpath("//*[text()='I am a Fresher']").click()
ch_browser.find_element_by_id("fname").send_keys("Stephen")
ch_browser.find_element_by_id("email").send_keys("rpaulpj88888@gmail.com")
ch_browser.find_element_by_name("password").send_keys("R6j35h@123")
ch_browser.find_element_by_name("number").send_keys("12345678")

ch_browser.find_element_by_name("city").send_keys("Thrissur")
ch_browser.find_element_by_name("city").send_keys(Keys.ARROW_DOWN)
ch_browser.find_element_by_name("city").send_keys(Keys.ENTER)



# obj = Select(ch_browser.find_element_by_name("city"))
# obj.select_by_visible_text("Thrissur")


ch_browser.find_element_by_name("uploadCV").send_keys("C:/Users/Guest User/Desktop/RAJESH/RAJESH_Resume April 2019.pdf")
# ch_browser.find_element_by_name("basicDetailSubmit").click()
