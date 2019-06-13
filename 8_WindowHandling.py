import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://phptravels.com/")

time.sleep(10)

# driver.find_element_by_class_name("login").click().........Less specific region
driver.find_element_by_xpath("//*[text()='Login']").click()

print("Current window -->",driver.current_window_handle)

CW=driver.current_window_handle  # Returns the current window

WH=driver.window_handles   # Returns all windows within the current session.Return type will be 'List'
print(WH)

for i in WH:
    if i!=CW:
        driver.switch_to.window(i) # To switch control to new window

driver.find_element_by_id("inputEmail").send_keys("abc@123")

# driver.close() # --->Closes currently active window
# driver.quit() # --->Closes currently active browser session

