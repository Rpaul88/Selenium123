# import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:/WebDrivers/chromedriver")

driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
# driver.implicitly_wait(10)

# driver.find_element_by_id("datepicker").click()

# Identification of iframe & switching to it.
# <iframe src="/resources/demos/datepicker/dropdown-month-year.html" class="demo-frame">
framevar = driver.find_element_by_xpath("//iframe[@class='demo-frame']") # Or //*[@class='demo-frame']
driver.switch_to.frame(framevar)

driver.find_element_by_xpath("//input[@class='hasDatepicker']").click()  # <input type="test" id="datepicker" class="hasDatepicker">
# OR driver.find_element_by_id("datepicker").click()
# OR driver.find_element_by_class_name("hasDatepicker").click()

month = driver.find_element_by_class_name("ui-datepicker-month")
s1 = Select(month)
s1.select_by_visible_text("Mar") # <option value="4">May</option>

year = driver.find_element_by_class_name("ui-datepicker-year")
s2=Select(year)
s2.select_by_value("2010") # <option value="2010">2010</option>

driver.find_element_by_xpath("//a[text()='3']").click() # <a class="ui-state-default" href="#">3</a>