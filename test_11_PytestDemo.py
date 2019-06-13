import time

from selenium import webdriver

def test_login():

    driver = webdriver.Chrome()
    driver.get("http://testing-ground.scraping.pro/login")
    time.sleep(3)
    driver.find_element_by_id("usr").send_keys("admin")
    time.sleep(3)
    driver.find_element_by_id("pwd").send_keys("12345")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@type='submit']").click()
    time.sleep(3)

def test_login1():

    # driver = webdriver.Chrome()
    driver.get("http://testing-ground.scraping.pro/login")
    time.sleep(3)
    driver.find_element_by_id("usr").send_keys("admin")
    time.sleep(3)
    driver.find_element_by_id("pwd").send_keys("12345")
    time.sleep(3)
    driver.find_element_by_xpath("//*[@type='submit']").click()
    time.sleep(3)

###########################################################################

# Install pytest package
# Install pytest-html package---->To generate .html file

# Conditions to run pytest.
# 1.File name----> test_11_PytestDemo.py
# 2.Method name--->test_test_login1()
# Note--> No need to call the method for execution

# To execute testscripts
# 1. Right click on project--->Open in TErminal
# python -m pytest
# python -m pytest -v ( Detailed report

# To generate pytest html report
# python -m pytest --html report.html









