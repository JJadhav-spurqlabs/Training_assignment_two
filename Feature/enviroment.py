import time
from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.BMI_calculatorPage import BMI_Calculator_Page
import json


data = json.load(open("resources/config.json"))


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.get(data['WEB_URL'])
    context.driver.maximize_window()
    basepage = BasePage(context.driver)
    context.Bmi_calpage = BMI_Calculator_Page(basepage)
    time.sleep(2)


def after_all(context):
    context.driver.close()
