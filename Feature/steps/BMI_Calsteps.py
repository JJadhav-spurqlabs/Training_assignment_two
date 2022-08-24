from behave import *
from Feature.enviroment import *
use_step_matcher("re")


@given("User is on BMI calculator page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.calculator.net/bmi-calculator.html?ctype=metric')
    context.driver.maximize_window()


@when("user click on (?P<Age>.+)")
def step_impl(context, Age):
    context.Bmi_calpage.click_age(Age)


@step("select (?P<Gender>.+)")
def step_impl(context, Gender):
    context.Bmi_calpage.click_gender(Gender)


@step("enter (?P<Height>.+)")
def step_impl(context, Height):
    context.Bmi_calpage.click_Height(Height)


@step("User enter (?P<Weight>.+)")
def step_impl(context, Weight):
    context.Bmi_calpage.click_weight(Weight)


@step("clicks on Calculate button")
def step_impl(context):
    context.Bmi_calpage.click_cal_button()


@then("verify the (?P<Result>.+)")
def step_impl(context, Result):
    resobj = context.Bmi_calpage.result()
    assert resobj==Result



