import time

import allure
from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig

'''
    This page includes locators and functions of user creation and user management page

    '''


class CustomPlan(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'plan_success')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _create_plan = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary css-3rsm85' and contains(text(),'Create')]"
    _plan_name = "//input[@name='plan_name']"
    _plan_desc = "//textarea[@name='plan_description']"
    calender_icon = "//button[@aria-label='Choose date']"
    _expand_year = "//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium MuiPickersCalendarHeader-switchViewIcon css-sldnni']"
    _select_year = "//button[normalize-space()='2026']"
    _select_date = "//button[normalize-space()='2']"
    _set_default = "//span[text()='Set as Default Plan']/preceding-sibling::span/input[@type='checkbox']"
    _license_for_hiring = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Hiring')]"
    _license_for_labs = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Labs')]"
    _license_for_lxp = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy LXP')]"
    _license_for_assessments = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Assessment')]"
    _labs_no_of_users = "//input[@name='plan_details.0.isChecked']"
    _no_of_users_quantity= "//input[@name='plan_details.0.quantity']"
    _job_post_check = "//input[@name='plan_details.10.isChecked']"
    _job_post_quantity = "//input[@name='plan_details.10.quantity']"
    _create_plan_confirm ="//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary css-3rsm85' and contains(text(),'Create')]"
    _success_msg = "//div[@id='notistack-snackbar']"
    _check_plan_details = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary css-3rsm85' and contains(text(),'Check')]"
    _activate_plan = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary css-3rsm85' and contains(text(),'Activate')]"

    def clickOnCreate(self):
        self.element_click(self._create_plan,"xpath")

    def enterPlanName(self,data):
        self.wait_for_element(self._plan_name, "xpath")
        self.element_click(self._plan_name,"xpath")
        self.send_keys(data, self._plan_name, "xpath")

    def enterPlanDes(self,data):
        self.element_click(self._plan_desc, "xpath")
        self.send_keys(data, self._plan_desc, "xpath")

    def selectDate(self):
        self.element_click(self.calender_icon, "xpath")
        self.wait_for_element(self._expand_year, "xpath")
        self.element_click(self._expand_year, "xpath")
        self.wait_for_element(self._select_year, "xpath")
        self.element_click(self._select_year, "xpath")
        self.wait_for_element(self._select_date, "xpath")
        self.element_click(self._select_date, "xpath")

    def setDefaultPlan(self):
        self.element_click(self._set_default,"xpath")

    def expandLabs(self):
        self.element_click(self._license_for_labs,"xpath")

    def expandHiring(self):
        self.wait_till_element_invisibility("//div[@class='base-Popper-root MuiPickersPopper-root css-1mtsuo7']","xpath")
        self.element_click(self._license_for_hiring,"xpath")

    def setNoOfUsers(self):
        time.sleep(5)
        #self.waitForElement(self._labs_no_of_users,"xpath")
        self.element_click_js(self._labs_no_of_users,"xpath")
        time.sleep(2)
        self.element_click_js(self._no_of_users_quantity,"xpath")
        self.send_keys("5", self._no_of_users_quantity, "xpath")

    def setJobPost(self):
        self.wait_for_element(self._job_post_check, "xpath")
        self.element_click(self._job_post_check, "xpath")
        self.element_click(self._job_post_quantity, "xpath")
        self.send_keys("5", self._job_post_quantity, "xpath")

    def setLabs(self):
        self.expandLabs()
        self.setNoOfUsers()

    def setHiring(self):
        self.expandHiring()
        self.setJobPost()

    def clickCreatePlan(self):
        self.element_click(self._create_plan_confirm,"xpath")

    def clickOnCheckPlanDetails(self):
        self.element_click(self._check_plan_details,"xpath")

    def clickOnActivatePlan(self):
        self.element_click(self._activate_plan,"xpath")

    def CreateDefaultPlan(self,Plan_name,Plan_desc):
        self.clickOnCreate()
        self.enterPlanName(Plan_name)
        self.enterPlanDes(Plan_desc)
        self.selectDate()
        self.setDefaultPlan()
        self.setLabs()
        self.setHiring()
        self.clickCreatePlan()
        time.sleep(5)

    def CreateCustomPlan(self,Plan_name,Plan_desc):
        self.clickOnCreate()
        self.enterPlanName(Plan_name)
        self.enterPlanDes(Plan_desc)
        self.web_scroll("down")
        self.setLabs()
        self.selectDate()
        self.clickCreatePlan()

    def verifyPlanCreation(self):
        self.verify_by_comparing_text(self._success_msg,"xpath",self.expected_result,"PlanCreationTest")


    def verifyCheckDetails(self):
        self.verify_by_element_presence("//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-1kzuk0']","xpath","PlanDetailsTest")


    def verifyPlanActivation(self):
        self.verify_by_comparing_text(self._success_msg,"xpath","Plan Activated Successfully","PlanActivationTest")


