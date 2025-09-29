"""
    This page includes locators and functions of AuditLogs Page

    """
import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig


class AuditLogs(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'Logs_message')
    expected_result1 = ReadConfig.get_expected_result(section='Expected Results', opt= 'Log_Filter_Error_Message1')
    expected_result2 = ReadConfig.get_expected_result(section='Expected Results', opt='Log_Filter_Error_Message2')
    # start_date = ReadConfig.get_start_date()
    # end_date = ReadConfig.get_end_date()
    user_name = ReadConfig.get_username('Audit Logs', 'user_name')




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _Filter_button = "(//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary css-3rsm85'][1])"
    _Type_dropdown = "//div[@class='MuiSelect-select MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input css-pkbdyv']"  #"//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium MuiSelect-icon MuiSelect-iconOutlined css-m9m7cd']"
    _Type_dropdown_option = "(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-ht1cav'])[1]"
    _Tenant_Name_dropdown = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium MuiAutocomplete-popupIndicator css-uge3vf']"#"//div[@class='MuiAutocomplete-endAdornment css-mxlkbn']"
    _Tenant_Name_dropdown_option = "//li[contains(@id,'option-3')]"
    _Start_date = "(//input[@placeholder='DD/MM/YYYY'])[1]"
    _clear_element = "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium clearButton css-1yxmbwk'])[1]"
    _cancel_icon = "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium clearButton css-1yxmbwk'])[2]"
    _End_date = "(//input[@placeholder='DD/MM/YYYY'])[2]"
    _Apply_filter_button = "(//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary css-3rsm85'])[3]"
    _LXP_tab = "//div[normalize-space()='LXP']"
    _Labs_tab = "//div[normalize-space()='Labs']"
    _Assesments_tab = "//div[normalize-space()='Assesments']"
    _Hiring_tab = "//div[normalize-space()='Hiring']"
    _Export_tab = "//button[normalize-space()='Export']"
    _search_tab = "//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1b6xge3']"
    _Filter_message = "//div[contains(text(),'User Name')]"
    _Text_message = "//h3[@class='MuiTypography-root MuiTypography-h3 css-kkhisd']"
    _Filter_Error_Message = "//div[@class='go946087465']"
    _Filter_Error_Message2 = "//div[@class='go1888806478 notistack-MuiContent notistack-MuiContent-error go167266335 go3651055292 go3162094071']"

    def SearchUser(self,user_name):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._search_tab, "xpath")
        self.send_keys(user_name, self._search_tab, "xpath")

    def clickOnLXPTab(self):
        self.wait_for_element(self._LXP_tab, "xpath")
        self.element_click(self._LXP_tab, locator_type="xpath")

    def clickOnLabsTab(self):
        self.wait_for_element(self._Labs_tab, locator_type="xpath")
        self.element_click(self._Labs_tab, locator_type="xpath")

    def clickOnAssesmentsTab(self):
        self.wait_for_element(self._Assesments_tab, locator_type="xpath")
        self.element_click(self._Assesments_tab, locator_type="xpath")

    def clickOnHiringTab(self):
        self.wait_for_element(self._Hiring_tab, locator_type="xpath")
        self.element_click(self._Hiring_tab, locator_type="xpath")

    def clickOnFilterbutton(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Filter_button, locator_type="xpath")

    def clickOnTypeDropdown(self):
        self.element_click(self._Type_dropdown, "xpath")

    def selectTypeDropdown(self):
        self.element_click(self._Type_dropdown_option, locator_type="xpath")

    def clickOnTenantNamedropdown(self):
        self.wait_for_element(self._Tenant_Name_dropdown, "xpath")
        self.element_click(self._Tenant_Name_dropdown, locator_type="xpath")

    def selectTenantNameoption(self):
        self.element_click(self._Tenant_Name_dropdown_option, locator_type="xpath")

    def enterStartDate(self):
        self.wait_for_element(self._Start_date, locator_type="xpath")
        self.element_click(self._Start_date, "xpath")
        date = self.get_current_ddmmyyyy(-15)
        self.send_keys(date, self._Start_date, "xpath")

    def enterEndDate(self):
        self.wait_for_element(self._End_date, "xpath")
        self.element_click(self._End_date, "xpath")
        date = self.get_current_ddmmyyyy(0)
        self.send_keys(date, self._End_date, locator_type="xpath")

    def clearbutton(self):
        self.element_click(self._clear_element, "xpath")

    def cancelicon(self):
        self.element_click(self._cancel_icon, "xpath")

    def clickOnApplyFilter(self):
        self.element_click(self._Apply_filter_button, locator_type="xpath")


    def clickOnExportTab(self):
        #self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.wait_for_element(self._Export_tab, locator_type="xpath")
        self.element_click(self._Export_tab, locator_type="xpath")

    def selectDates(self):
        self.enterStartDate()
        self.enterEndDate()


    def VerifyAllProductLogs(self):
        self.clickOnLXPTab()
        self.clickOnLabsTab()
        self.clickOnAssesmentsTab()
        self.clickOnHiringTab()

    def VerifyApplyFilter(self):
        self.clickOnFilterbutton()
        self.clickOnTypeDropdown()
        self.selectTypeDropdown()
        self.clickOnTenantNamedropdown()
        self.selectTenantNameoption()
        time.sleep(2)
        self.selectDates()
        self.clickOnApplyFilter()

    def ApplyFilterNegative(self):
        self.clickOnFilterbutton()
        self.enterStartDate()
        self.clickOnApplyFilter()

    def VerifyExport(self):
        self.clickOnExportTab()


    def VerifySearch(self):
        self.SearchUser(self.user_name)

    def verifyLogs(self):
        self.verify_by_comparing_text(locator=self._Text_message, locator_type="xpath", expected_result=self.expected_result, result_msg="Audit Logs")


    def VerifyApplyFilterNegative1(self):
        self.verify_by_comparing_text(locator=self._Filter_Error_Message, locator_type = "xpath", expected_result=self.expected_result1, result_msg = "Please select at least one filter.")


    def VerifyApplyFilterNegative2(self):
        self.verify_by_comparing_text(locator=self._Filter_Error_Message2, locator_type = "xpath", expected_result=self.expected_result2, result_msg = "Please select both start date and end date.")