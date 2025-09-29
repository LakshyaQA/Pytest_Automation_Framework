"""
    This page includes locators and functions of Reports page

    """
import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig


class Report(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'Download_Report')
    expected_result_tenant = ReadConfig.get_expected_result('Expected Results', 'Reports_success')
    expected_result_error_Message1 = ReadConfig.get_expected_result(section='Expected Results',
                                                                   opt='Report_Error_Message1')
    expected_result_error_Message2 = ReadConfig.get_expected_result(section='Expected Results',
                                                                    opt='Report_Error_Message2')
    gmail_username = ReadConfig.get_username('Report Mail', 'username')
    gmail_password = ReadConfig.get_username('Report Mail', 'password')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cl = cl.custom_logger()

    # Locators
    _Tenant_name_dropdown = ("(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd "
                             "MuiAutocomplete-input MuiAutocomplete-inputFocused css-1b6xge3'])[1]")
    _Tenant_name_option = "//li[contains(@id,'option-12')]"
    _Business_unit_dropdown = "(//div[@class='MuiAutocomplete-endAdornment css-mxlkbn'])[2]"
    _Tenant_BU = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium "
                  "MuiAutocomplete-popupIndicator css-uge3vf'])[1]")
    _bu_option = "//li[contains(@id,'option-0')]"
    _Start_date = "(//input[@placeholder='DD/MM/YYYY'])[1]"
    _clear_element = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium clearButton "
                      "css-1yxmbwk'])[1]")
    _cancel_icon = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium clearButton "
                    "css-1yxmbwk'])[2]")
    _End_date = "(//input[@placeholder='DD/MM/YYYY'])[2]"
    _Product_name_dropdown = "(//div[@class='MuiAutocomplete-endAdornment css-mxlkbn'])[3]"
    _Tenant_ProductName_dropdown = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium "
                                    "MuiAutocomplete-popupIndicator css-uge3vf'])[2]")
    _Product_name_option1 = "//li[contains(@id,'option-0')]"
    _Product_name_option2 = "//li[contains(@id,'option-1')]"
    _Product_name_option3 = "//li[contains(@id,'option-2')]"
    _Product_name_option4 = "//li[contains(@id,'option-3')]"
    _Report_type_dropdown = "(//div[@class='MuiAutocomplete-endAdornment css-mxlkbn'])[4]"
    _Tenant_report_type_dropdown = "(//div[@class='MuiAutocomplete-endAdornment css-mxlkbn'])[3]"
    _Report_type_option1 = "//li[contains(@id,'option-0')]"
    _Report_type_option2 = "//li[contains(@id,'option-1')]"
    _Report_type_option3 = "//li[contains(@id,'option-2')]"
    _Report_type_option4 = "//li[contains(@id,'option-3')]"
    _Report_type_option5 = "//li[contains(@id,'option-4')]"
    _Report_type_option6 = "//li[contains(@id,'option-5')]"
    _Report_type_option7 = "//li[contains(@id,'option-6')]"
    _Report_name = "//input[@name='report_name']"
    _Generate_report_btn = "//button[normalize-space()='Generate Reports']"
    _Download_report_btn = "(//h6[@class='MuiTypography-root MuiTypography-h6 css-1loe7ol'])[6]"
    _check_box = "//input[@type='checkbox']"
    _actual_result = "//h2[@class='hP']"
    _username_field = "//input[@autocomplete='username']"
    _next_button1 = ("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc "
                     "AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
    _password_field = "//input[@type='password']"
    _next_button2 = "//span[normalize-space()='Next']"
    _mail = "(//div[@class='y6'])[1]"
    _mail1 = "(//div[@class='iA g6'])[2]"
    _download_report_btn = "(//a[contains(text(),'Download Report')])[1]"
    _Report_Generation_Success = ("//div[contains(text(),'Report generation is in progress. Once it is completed, "
                                  "an email will be sent.')]")
    _Report_Generation_Error1 = "//div[@class='go946087465']"
    _Report_Generation_Error2 = "(//p[@class='MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium MuiFormHelperText-contained MuiFormHelperText-filled css-1pie0bz'])[1]"

    def selectTenant(self):
        self.wait_till_element_invisibility("//div[@class='MuiStack-root css-dvxtzn']", "xpath")
        self.select_element(self._Tenant_name_dropdown, self._Tenant_name_option, locator_type="xpath")

    def clickOnBUDropdown(self):
        self.wait_for_element(self._Business_unit_dropdown, locator_type="xpath")
        self.element_click(self._Business_unit_dropdown, "xpath")

    def clickOnBUDropdown1(self):
        self.wait_for_element(self._Tenant_BU, locator_type="xpath")
        self.element_click(self._Tenant_BU, locator_type="xpath")

    def selectBusinessUnitDropdown(self):
        self.wait_for_element(self._bu_option, "xpath")
        self.element_click(self._bu_option, locator_type="xpath")

    def clearbutton(self):
        self.element_click(self._clear_element, "xpath")

    def cancelicon(self):
        self.element_click(self._cancel_icon, "xpath")

    def enterStartDate(self):
        self.wait_for_element(self._Start_date, locator_type="xpath")
        date = self.get_current_ddmmyyyy(-15)
        self.send_keys(date, self._Start_date, "xpath")


    def enterEndDate(self):
        self.wait_for_element(self._End_date, locator_type="xpath")
        date = self.get_current_ddmmyyyy(0)
        self.send_keys(date, self._End_date, "xpath")

    def enterStartDate1(self):
        self.wait_for_element(self._Start_date, locator_type="xpath")
        date = self.get_current_ddmmyyyy(0)
        self.send_keys(date, self._Start_date, "xpath")


    def enterEndDate1(self):
        self.wait_for_element(self._End_date, locator_type="xpath")
        date = self.get_current_ddmmyyyy(-1)
        self.send_keys(date, self._End_date, "xpath")

    def clickOnTenantProdDropdown(self):
        self.wait_for_element(self._Tenant_ProductName_dropdown, "xpath")
        self.element_click(self._Tenant_ProductName_dropdown, locator_type="xpath")

    def clickOnProdDropdown(self):
        self.wait_for_element(self._Product_name_dropdown, "xpath")
        self.element_click(self._Product_name_dropdown, "xpath")

    def selectProductNames(self):
        self.element_click(self._Product_name_option1, "xpath")
        self.element_click(self._Product_name_option2, "xpath")
        self.element_click(self._Product_name_option3, "xpath")
        self.element_click(self._Product_name_option4, "xpath")


    def clickOnReportDropdown(self):
        self.element_click(self._Report_type_dropdown, "xpath")

    def clickonTenantReportDropdown(self):
        self.element_click(self._Tenant_report_type_dropdown, locator_type="xpath")

    def selectReportTypes(self):
        self.element_click(self._Report_type_option1, "xpath")
        self.element_click(self._Report_type_option2, "xpath")
        self.element_click(self._Report_type_option3, "xpath")
        self.element_click(self._Report_type_option4, "xpath")
        self.element_click(self._Report_type_option5, "xpath")
        self.element_click(self._Report_type_option6, "xpath")


    def enterReportname(self, reportname):
        random_name = self.generate_random_name(reportname)
        self.wait_for_element(self._Report_name, locator_type="xpath")
        self.send_keys(random_name, self._Report_name, locator_type="xpath")

    def clickOnGenerateReport(self):
        self.wait_for_element(self._Generate_report_btn, locator_type="xpath")
        self.element_click_js(self._Generate_report_btn, "xpath")
        self.wait_for_page_load()

    def selectDates(self):
        self.clearbutton()
        self.enterStartDate()
        self.cancelicon()
        self.enterEndDate()


    def selectDates1(self):
        self.clearbutton()
        self.enterStartDate1()
        self.cancelicon()
        self.enterEndDate1()

    def downloadReport(self):
        self.wait_for_element(self._Download_report_btn, locator_type="xpath")
        self.element_click(self._Download_report_btn, locator_type="xpath")

    def clickUsername(self):
        self.wait_for_element(self._username_field, locator_type="xpath")
        self.element_click(self._username_field, locator_type="xpath")

    def clickPassword(self):
        self.wait_for_element(self._password_field, locator_type="xpath")
        self.element_click(self._password_field, locator_type="xpath")

    def enterUsername(self, username):
        self.wait_for_element(self._username_field, locator_type="xpath")
        self.send_keys(username, self._username_field, locator_type="xpath")

    def clickNext1(self):
        self.wait_for_element(self._next_button1, locator_type="xpath")
        self.element_click(self._next_button1, locator_type="xpath")

    def enterPassword(self, password):
        self.wait_for_element(self._password_field, locator_type="xpath")
        self.send_keys(password, self._password_field, locator_type="xpath")

    def clickNext2(self):
        self.wait_for_element(self._next_button2, locator_type="xpath")
        self.element_click(self._next_button2, locator_type="xpath")

    def clickOnMail(self):
        self.wait_for_element(self._mail, locator_type="xpath")
        self.element_click(self._mail, locator_type="xpath")

    def clickOnmail1(self):
        self.wait_for_element(self._mail, locator_type="xpath")
        self.element_click(self._mail1, locator_type="xpath")

    def clickOnDownloadReport(self):
        self.wait_for_element(self._download_report_btn, locator_type="xpath")
        self.element_click(self._download_report_btn, locator_type="xpath")

    def verifyEmailNotification(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.gmail.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.refresh_page()
        self.clickUsername()
        self.enterUsername(self.gmail_username)
        self.clickNext1()
        self.clickPassword()
        self.enterPassword(self.gmail_password)
        self.clickNext2()
        self.clickOnMail()
        self.clickOnmail1()
        self.clickOnDownloadReport()

    def ReportGeneration(self, name):
        self.selectTenant()
        # self.clickOnBUDropdown()
        # self.selectBusinessUnitDropdown()
        self.selectDates()
        self.clickOnProdDropdown()
        self.selectProductNames()
        self.clickOnReportDropdown()
        self.selectReportTypes()
        self.enterReportname(name)
        self.clickOnGenerateReport()
        # time.sleep(30)
        # self.refresh_page()
        # self.downloadReport()

    def ReportGenerationNegative1(self, name):
        self.selectTenant()
        self.clickOnBUDropdown()
        self.selectBusinessUnitDropdown()
        self.selectDates1()
        self.clickOnProdDropdown()
        self.selectProductNames()
        self.clickOnReportDropdown()
        self.selectReportTypes()
        self.enterReportname(name)
        self.clickOnGenerateReport()

    def ReportGenerationNegative2(self, name):
        self.selectTenant()
        self.clickOnBUDropdown()
        self.selectBusinessUnitDropdown()
        #self.selectDates()
        self.clickOnProdDropdown()
        self.selectProductNames()
        self.clickOnReportDropdown()
        self.selectReportTypes()
        self.enterReportname(name)
        self.clickOnGenerateReport()

    def ReportGenerationTenant(self, name):
        self.clickOnBUDropdown1()
        self.selectBusinessUnitDropdown()
        self.selectDates()
        self.clickOnTenantProdDropdown()
        self.selectProductNames()
        self.clickonTenantReportDropdown()
        self.selectReportTypes()
        self.enterReportname(name)
        self.clickOnGenerateReport()

    def VerifyReportGeneration(self):
        self.verify_by_comparing_text(locator=self._actual_result, locator_type="xpath",
                                      expected_result=self.expected_result, result_msg="Download Your Report")

    def VerifyReportGenerationError1(self):
        self.verify_by_comparing_text(locator=self._Report_Generation_Error1, locator_type="xpath",
                                      expected_result=self.expected_result_error_Message1, result_msg="from date cannot be "
                                                                                                     "previous than tenant "
                                                                                                     "creation date")

    def VerifyReportGenerationError2(self):
        self.verify_by_comparing_text(locator=self._Report_Generation_Error2, locator_type="xpath",
                                      expected_result=self.expected_result_error_Message2,
                                      result_msg="This field is required")


    def VerifyReportGenerationTenant(self):
        self.verify_by_comparing_text(locator=self._Report_Generation_Success, locator_type="xpath",
                                      expected_result=self.expected_result_tenant, result_msg="Report generation is in "
                                                                                              "progress. Once it is "
                                                                                              "completed, an email "
                                                                                              "will be"
                                                                                              "sent.")
