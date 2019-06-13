from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Guest%20User/Desktop/RAJESH/Selenium/TableHandling.html")

row_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr") # All rows {(1,A,100) , (2,B,200), (3,C,300) }
row_count = len(row_val)

fp = "//*[@id='123']/tbody/tr["
sp="]/td[1]"

for i in range(1,row_count+1):
    id_val = driver.find_element_by_xpath(fp+str(i)+sp).text
    if int(id_val)==4:
        sal_val=driver.find_element_by_xpath(fp+str(i)+"]/td[3]").text
        print("Salary of emp id " + id_val + " = ",sal_val)
