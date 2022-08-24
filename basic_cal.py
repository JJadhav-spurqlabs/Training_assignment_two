import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.calculator.net')
driver.maximize_window()
time.sleep(2)

a = driver.find_element(By.XPATH,"//*[text()='4']")
a.click()
time.sleep(2)

ope = driver.find_element(By.XPATH,"//*[text()='+']")
ope.click()
time.sleep(2)

b = driver.find_element(By.XPATH,"//*[text()='5']")
b.click()
time.sleep(2)

res = driver.find_element(By.XPATH,"//*[@id='sciOutPut']").text
res.lstrip()
print(res)

driver.close()

