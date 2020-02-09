from unittest import TestCase
from selenium import webdriver

driver = webdriver.Chrome("drivers/chromedriver.exe")

driver.set_page_load_timeout(20)

driver.maximize_window()

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

driver.find_element_by_xpath(".//input[@id='sum1']").send_keys('4')

driver.find_element_by_xpath(".//input[@id='sum2']").send_keys('5')

driver.find_element_by_xpath(".//*[text()='Get Total']").click()

sumOut = int(driver.find_element_by_xpath(".//*[@id='displayvalue']").text)

t = TestCase()
t.assertEqual(sumOut, 9, "Values are not matching")

driver.quit()


