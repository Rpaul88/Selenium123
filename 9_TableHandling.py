from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///C:/Users/Guest%20User/Desktop/RAJESH/Selenium/TableHandling.html")

# To fetch 1st row data
# ele=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")

# To fetch 1st row,first column element
# ele=driver.find_element_by_xpath("//*[@id='123']/tbody/tr[1]/td[1]")

# To fetch 1st row, 3rd column element
# ele=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[3]/td[2]")

# To fetch all elements in 1st column
# ele=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td")

# To fetch all elements in table row wise
# ele=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr")

# To fetch all elements in table one by one, column wise
# ele=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr/td")

# print(ele)
# print(len(ele))
#
# for i in ele:
#     print(i.text)

##----------------------------------------------------------------##

# To find row count & column count

col_val=driver.find_elements_by_xpath("//*[@id='123']/tbody/tr[1]/td") # All elements in 1st row(1,A,100)
col_count=len(col_val)
print("Column count is",col_count)

row_val = driver.find_elements_by_xpath("//*[@id='123']/tbody/tr") # All rows {(1,A,100) , (2,B,200), (3,C,300) }
row_count = len(row_val)
print("Row count is", row_count)

##-----------------------------------------------------------------##

# To print web elements in 1st row

fp="//*[@id='123']/tbody/tr[1]/td["
sp="]"
for i in range(1,col_count+1):
    final_p = fp + str(i) + sp
    w=driver.find_element_by_xpath(final_p).text
    print(w)

##########################################################################



