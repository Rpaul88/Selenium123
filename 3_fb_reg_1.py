from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

browser='chrome'

if(browser=='chrome'):
    driver=webdriver.Chrome() #(executable_path="C:/WebDrivers/chromedriver")

elif(browser=='FF'):
    driver=webdriver.Firefox(executable_path="C:/      /geckodriver.exe")

elif(browser=='IE'):
    driver=webdriver.Ie(executable_path="C:/WebDrivers/IEDriverServer")

driver.get("https://www.facebook.com")

driver.find_element_by_name("firstname").send_keys("Raj") #FirstName
driver.find_element_by_name("lastname").send_keys("Sharma") #SecondName
driver.find_element_by_xpath("//*[contains(@aria-label,'Mobile number')]").send_keys("9495855466") #aria-label="Mobile number or email address"
driver.find_element_by_xpath("//*[@aria-label='New password']").send_keys("rajesh123")             #aria-label="New password"


# driver.find_element_by_name("birthday_day").send_keys("24")
# driver.find_element_by_id("month").send_keys("Sept")
# driver.find_element_by_id("year").send_keys("1990")

# Dropdown selection(visible_text,Value,index)

s1=Select(driver.find_element_by_name("birthday_day"))
s1.select_by_visible_text("24")

s2=Select(driver.find_element_by_id("month"))
s2.select_by_value("9")                             # <option value="9">Sept</option>

s3=Select(driver.find_element_by_id("year"))
s3.select_by_index("30")                            # Index value considering 'Year' value


driver.find_element_by_xpath("//input[@value='2']").click()
#driver.find_element_by_name("websubmit").click()


