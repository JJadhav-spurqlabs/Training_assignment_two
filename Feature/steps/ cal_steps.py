import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("open calculator home")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.calculator.net')
    context.driver.maximize_window()
    time.sleep(1)


@when("i enter following data from table")
def step_impl(context):
    numb1 = context.table[0][0]
    print('numb1:',numb1)
    for n in range(0,len(numb1)):
        context.driver.find_element(By.XPATH, "//*[text()='"+numb1[n]+"']").click()
        time.sleep(2)

    plusop = context.table[0][1]
    context.driver.find_element(By.XPATH, "//*[text()='" +plusop+ "']").click()
    time.sleep(2)

    numb2 = context.table[0][2]
    print('numb2:',numb2)
    for m in range(0, len(numb2)):
        context.driver.find_element(By.XPATH, "//*[text()='" + numb1[m] + "']").click()
        time.sleep(20)


    result = context.table[0][3]
    res = context.driver.find_element(By.XPATH, "//*[@id='sciOutPut']").text
    print('res:',res)
    assert res==result
