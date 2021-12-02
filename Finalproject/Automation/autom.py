from selenium import webdriver
import time

print("test case started")

driver = webdriver.Chrome("C://Users//user//Downloads//chromedriver_win32 (1)//chromedriver.exe")

driver.maximize_window()

driver.delete_all_cookies()

driver.get("http://127.0.0.1:5000/")
time.sleep(2)

driver.find_element_by_id("name").send_keys("Anjana")
time.sleep(5)
driver.find_element_by_id("uid").send_keys("191800")
time.sleep(5)
driver.find_element_by_id("cname").send_keys("Ust")
time.sleep(5)
driver.find_element_by_id("cmail").send_keys("an@gmail.com")
time.sleep(5)
driver.find_element_by_id("password").send_keys("1234")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div[2]/form/button").click()
time.sleep(5)
driver.close()
print("Ust login has been successfully completed")