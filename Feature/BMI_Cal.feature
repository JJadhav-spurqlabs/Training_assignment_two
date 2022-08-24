# Created by jjadh at 17-08-2022
Feature: BMI Calculator functionality

  Scenario Outline: : BMI(Body Mass Index)
#    Given User is on BMI calculator page
    When user click on <Age>
    And select <Gender>
    And enter <Height>
    And User enter <Weight>
    And clicks on Calculate button
    Then verify the <Result>
    Examples:
      | Age | Gender | Height | Weight | Result           |
      | 20  | Male   | 180    | 60     | BMI = 18.5 kg/m2 |
      | 35  | Female | 160    | 55     | BMI = 21.5 kg/m2 |
      | 50  | Male   | 175    | 65     | BMI = 21.2 kg/m2 |
      | 45  | Female | 150    | 52     | BMI = 23.1 kg/m2 |


























