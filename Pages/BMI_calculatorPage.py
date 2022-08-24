from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import time

class BMI_Calculator_Page:
    def __init__(self,context):
        BasePage.__init__(self,context.driver)
        self.context = context
        self.Age = 'cage'
        self.Mgen = "//*[text()='Male']"
        self.Fgen = "//*[text()='Female']"
        self.Height = 'cheightmeter'
        self.Weight = 'ckg'
        self.Calbutton = '//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/input[2]'
        self.Result = "//*[@class='bigtext']"


    def click_age(self):
        self.driver.find_element(By.ID,'cage').click()
        time.sleep(2)

    def click_gender(self,Gender):
        self.driver.find_element(By.XPATH,"//*[text()='"+Gender+"']").click()
        time.sleep(2)

    def click_Height(self):
        self.driver.find_element(By.ID,'cheightmeter').click()
        time.sleep(2)

    def click_weight(self):
        self.driver.find_element(By.ID,'ckg').click()
        time.sleep(2)

    def click_cal_button(self):
        self.driver.find_element(By.XPATH,'//*[@id="content"]/div[4]/div[2]/table/tbody/tr/td/table[4]/tbody/tr/td/input[2]').click()
        time.sleep(2)

    def result(self,Result):
        result = self.driver.find_element(By.XPATH, "//*[@class='bigtext']").click()
        if result.get_attribute('value') == Result:
            print('result:', result)
            return result


