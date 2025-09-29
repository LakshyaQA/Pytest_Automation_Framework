import time

import allure
from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig

'''
    This page includes locators and functions of user creation and user management page

    '''


class Licensing(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'license_success')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _generate_license = "//button[normalize-space()='Generate License']"
    calender_icon = "(//button[@aria-label='Choose date'])[1]"
    _carry_over = "//input[@name='carry_over_percentage']"
    _license_for_hiring = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Hiring')]"
    _license_for_labs = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Labs')]"
    _license_for_lxp = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy LXP')]"
    _license_for_assessments = "//h4[@class='MuiTypography-root MuiTypography-h4 css-132c970' and contains(text(),'Techademy Assessment')]"
    _check_users_lab = "//input[@name='labs_licensing.0.isChecked']"
    _check_hours_lab = "//input[@name='labs_licensing.1.isChecked']"
    _users_quantity = "//input[@name='labs_licensing.0.value']"
    _hours_quantity = "//input[@name='labs_licensing.1.value']"
    _hiring_job_post_check = "//input[@name='hiring_licensing.0.isChecked']"
    job_post_quantity = "//input[@name='hiring_licensing.0.value']"
    _success_msg = "//div[@id='notistack-snackbar']"
    _expand_year = "//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium MuiPickersCalendarHeader-switchViewIcon css-sldnni']"
    _select_year = "//button[normalize-space()='2026']"
    _select_issue_date = "//button[normalize-space()='2']"
    _select_expiry_date = "//button[normalize-space()='5']"
    _activate_license = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1pl7tgk']"
    _confirmation_activate = "//button[normalize-space()='Yes, activate']"
    _active_status = "//span[@class='MuiChip-label MuiChip-labelMedium css-11lqbxm' and contains(text() ,'Active')]"
    _view_license = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1loe7ol' and contains(text(),'LI')]"
    _license_error = "//div[@id='notistack-snackbar' and contains(text(),'Cannot create a new license as previous license is not expired')]"



    def clickOnGenerate(self):
        self.wait_for_element(self._generate_license, "xpath")
        self.element_click_js(self._generate_license,"xpath")

    def selectIssueDate(self):
        self.wait_till_element_invisibility("//div[@class='loading']","xpath")
        self.element_click(self.calender_icon,"xpath")
        self.wait_for_element(self._expand_year, "xpath")
        self.element_click(self._expand_year,"xpath")
        self.wait_for_element(self._select_year, "xpath")
        self.element_click(self._select_year,"xpath")
        self.wait_for_element(self._select_issue_date, "xpath")
        self.element_click(self._select_issue_date,"xpath")

    def selectexpiryDate(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self.calender_icon, "xpath")
        self.wait_for_element(self._expand_year, "xpath")
        self.element_click(self._expand_year, "xpath")
        self.wait_for_element(self._select_year, "xpath")
        self.element_click(self._select_year, "xpath")
        self.wait_for_element(self._select_expiry_date, "xpath")
        self.element_click(self._select_expiry_date,"xpath")

    def selectLabs(self):
        self.element_click_js(self._license_for_labs,"xpath")

    def selectHiring(self):
        self.element_click_js(self._license_for_hiring,"xpath")

    def checkUsersLabs(self):
        self.element_click_js(self._check_users_lab,"xpath")

    def checkHoursLabs(self):
        self.element_click_js(self._check_hours_lab,"xpath")

    def checkHiringJob(self):
        self.element_click_js(self._hiring_job_post_check,"xpath")

    def enterUsersLab(self):
        self.wait_for_element(self._users_quantity, "xpath")
        self.element_click_js(self._users_quantity,"xpath")
        self.send_keys("5", self._users_quantity, "xpath")

    def enterHoursLab(self):
        self.wait_for_element(self._hours_quantity, "xpath")
        self.element_click_js(self._hours_quantity,"xpath")
        self.send_keys("6", self._hours_quantity, "xpath")

    def enterJobPost(self):
        self.wait_for_element(self.job_post_quantity, "xpath")
        self.element_click_js(self.job_post_quantity,"xpath")
        self.send_keys("7", self.job_post_quantity, "xpath")

    def setLabsLicense(self):
        self.selectLabs()
        self.checkUsersLabs()
        self.enterUsersLab()
        self.checkHoursLabs()
        self.enterHoursLab()

    def setHiringLicense(self):
        self.selectHiring()
        self.checkHiringJob()
        self.enterJobPost()

    def clickOnActivateLicense(self):
        self.element_click(self._activate_license,"xpath")

    def clickOnConfirmation(self):
        self.element_click(self._confirmation_activate,"xpath")

    def clickOnViewLicense(self):
        self.element_click(self._view_license,"xpath")

    def ActivateLicense(self):
        self.clickOnActivateLicense()
        self.clickOnConfirmation()

    def LicenseConfigure(self):
        self.clickOnGenerate()
        self.selectIssueDate()
        self.selectexpiryDate()
        self.setLabsLicense()
        self.setHiringLicense()
        self.clickOnGenerate()

    def verifyLicensing(self):
        self.verify_by_comparing_text(locator=self._success_msg, locator_type="xpath",expected_result=self.expected_result,result_msg="LicenseTest")

    def verifyActivateLicense(self):
        self.verify_by_element_presence(self._active_status,"xpath","ActivateLicenseTest")

    def verifyViewLicense(self):
        self.verify_by_element_presence("//h3[@class='MuiTypography-root MuiTypography-h3 css-kkhisd']","xpath","ViewLicenseTest")


    def verifyLicenseAlreadyexists(self):
        self.verify_by_element_presence(self._license_error,"xpath","LicenseAlreadyActive")