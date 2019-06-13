from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")

print("URL provided")

driver.implicitly_wait(30)

frame=driver.find_element_by_xpath("//*[@class='demo-frame']")
# frame=driver.find_element_by_class_name("demo-frame")
driver.switch_to.frame(frame)

print("Switch to iframe")

drag=driver.find_element_by_id("draggable")
print("Captured drag element")


drop=driver.find_element_by_id("droppable")
print("Captured drop element")


a = ActionChains(driver)
a.drag_and_drop(drag,drop).perform()
print("drag and drop completed")

# frame,drag,drop are variables
