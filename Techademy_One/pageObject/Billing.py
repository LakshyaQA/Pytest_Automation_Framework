import time

import allure
from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig

'''
    This page includes locators and functions of user creation and user management page

    '''


class BillingConfiguration(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'bill_configured')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _create_bill = "//button[normalize-space()='Create Bill']"
    _edit_bill = "//button[normalize-space()='Edit']"
    _cancel_btn = "//button[normalize-space()='Cancel']"
    _set_bill_btn = "//button[normalize-space()='Set Bill Parameters']"
    _update_bill_btn = "//button[normalize-space()='Update Bill Parameters']"
    _billing_cycle = "(//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input css-pkbdyv'])[1]"
    _monthly_option = "//li[@data-value='0']"
    _quarterly_option = "//li[@data-value='1']"
    _anually_option = "//li[@data-value='2']"
    _currency_dropdown = "(//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input css-pkbdyv'])[2]"
    _INR_option = "//li[@data-value='0']"
    _USD_option = "//li[@data-value='1']"
    _cgst_field = "//input[@name='gst_rates.cgst']"
    _sgst_field = "//input[@name='gst_rates.sgst']"
    _billing_model = "(//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input css-pkbdyv'])[3]"
    _fixed_option = "//li[@data-value='0']"
    _pay_per_use_option = "//li[@data-value='1']"
    _billing_for_hiring = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Hiring')]"
    _billing_for_labs = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Labs')]"
    _billing_for_lxp = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy LXP')]"
    _billing_for_assessments = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Assessment')]"
    _labs_pay_per_user = "//input[@name='labs_billing_points.pay_per_user']"
    _labs_pay_per_hr = "//input[@name='labs_billing_points.pay_per_hour']"
    _yaksha_mcq = "//input[@name='assessment_billing_points.knowledge_assessemt']"
    _yaksha_coding = "//input[@name='assessment_billing_points.coding_assessment']"
    _yaksha_project = "//input[@name='assessment_billing_points.project_assessment']"
    _yaksha_adaptive = "//input[@name='assessment_billing_points.adaptive_assessment']"
    _lxp_pay_per_user = "//input[@name='courses_billing_points.pay_per_user']"
    _lxp_pay_per_catalouge = "//input[@name='courses_billing_points.pay_per_catalogue']"
    _lxp_pay_per_course = "//input[@name='courses_billing_points.pay_per_course']"
    _lxp_pay_per_lp = "//input[@name='courses_billing_points.pay_per_learning_path']"
    _hiring_job_post = "//input[@name='hiring_billing_points.per_job_post']"
    _success_msg = "//div[@id='notistack-snackbar']"

    def clickOnCreateBill(self):
        self.element_click(self._create_bill,"xpath")

    def clickOnEditBill(self):
        self.element_click(self._edit_bill,"xpath")

    def clickOnCancel(self):
        self.element_click_js(self._cancel_btn,"xpath")

    def clickOnSetBill(self):
        self.element_click(self._set_bill_btn,"xpath")

    def clickOnUpdateBill(self):
        self.element_click(self._update_bill_btn,"xpath")

    def selectBillCycle(self):
        self.select_element(self._billing_cycle,self._monthly_option,"xpath")
        self.wait_till_element_invisibility("//div[@id='menu-billing_model_type']","xpath")

    def selectCurrency(self):
        self.select_element(self._currency_dropdown,self._INR_option,"xpath")
        self.wait_till_element_invisibility("//div[@id='menu-currency']", "xpath")


    def enterCGST(self):
        self.element_click(self._cgst_field,"xpath")
        self.send_keys('9', self._cgst_field, "xpath")

    def enterSGST(self):
        self.element_click(self._sgst_field,"xpath")
        self.send_keys('9', self._sgst_field, "xpath")

    def selectBillModel(self):
        self.select_element(self._billing_model,self._fixed_option,"xpath")
        self.wait_till_element_invisibility("//div[@id='menu-billing_model_type']", "xpath")

    def clickOnLabsBill(self):
        self.element_click(self._billing_for_labs,"xpath")

    def clickOnLXPBill(self):
        self.scroll_by_visible_element(self._billing_for_lxp,"xpath")
        self.element_click(self._billing_for_lxp,"xpath")

    def clickOnAssessmentBill(self):
        self.scroll_by_visible_element(self._billing_for_assessments,"xpath")
        self.element_click(self._billing_for_assessments,"xpath")

    def clickOnHiringBill(self):
        self.scroll_by_visible_element(self._billing_for_hiring,"xpath")
        self.element_click(self._billing_for_hiring,"xpath")

    def enterPayPerUserLabs(self):
        self.element_click(self._labs_pay_per_user,"xpath")
        self.send_keys('150', self._labs_pay_per_user, "xpath")

    def enterPayPerHour(self):
        self.element_click(self._labs_pay_per_hr,"xpath")
        self.send_keys('150', self._labs_pay_per_hr, "xpath")

    def setLabsBill(self):
        self.clickOnLabsBill()
        self.enterPayPerUserLabs()
        self.enterPayPerHour()

    def enterPayPerCourse(self):
        self.element_click(self._lxp_pay_per_course, "xpath")
        self.send_keys('120', self._lxp_pay_per_course, "xpath")

    def setLXPBill(self):
        self.clickOnLXPBill()
        self.enterPayPerCourse()

    def enterMCQ(self):
        self.element_click(self._yaksha_mcq,"xpath")
        self.send_keys('200', self._yaksha_mcq, "xpath")

    def setYakshaBill(self):
        self.clickOnAssessmentBill()
        self.enterMCQ()

    def enterJobPost(self):
        self.element_click(self._hiring_job_post,"xpath")
        self.send_keys('300', self._hiring_job_post, "xpath")

    def setHiringBill(self):
        self.clickOnHiringBill()
        self.enterJobPost()

    def SetBillParameters(self):
        self.clickOnCreateBill()
        self.selectBillCycle()
        self.selectCurrency()
        self.enterCGST()
        self.enterSGST()
        self.selectBillModel()
        self.setLabsBill()
        #self.setLXPBill()
        #self.setYakshaBill()
        self.setHiringBill()
        self.clickOnSetBill()


    def verifyBillConfiguration(self):
        self.verify_by_comparing_text(locator=self._success_msg, locator_type="xpath",expected_result=self.expected_result,result_msg="BillingTest")




