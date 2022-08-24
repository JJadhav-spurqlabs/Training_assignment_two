import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print('step1:open calculator')
driver = webdriver.Chrome()
driver.get('https://www.calculator.net/bmi-calculator.html?ctype=metric')
driver.maximize_window()


print('step2:enter age')
age = driver.find_element(By.ID,'cage')
age.clear()
age.send_keys(20)
time.sleep(2)


print('step3:select gender')
try:
    mgen = driver.find_element(By.XPATH,'//*[text()="Male"]')
    mgen.clear()
    mgen.click()
except:
    fgen = driver.find_element(By.XPATH,'//*[text()="Female"]')
    fgen.click()


print('step4:enter height')
height = driver.find_element(By.ID,"cheightmeter")
height.clear()
height.send_keys(180)
time.sleep(2)

print('step5:enter weight')
weight = driver.find_element(By.ID,"ckg")
weight.clear()
weight.send_keys(60)
time.sleep(2)

print('step6:click on calculate button')
cal = driver.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/input[2]')
cal.click()
time.sleep(2)


print('step7:verify result')
clr = driver.find_element(By.XPATH,'//*[@id="content"]/div[3]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/img')
clr.click()
time.sleep(2)

print('completed')

driver.close()



