"""
    This page includes locators and functions on create tenant page

    """

import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Techademy_One.configuration.read_properties import ReadConfig


class InvoiceGeneration(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'invoice_success')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators for Invoice list and Generation

    _generateinvoice = "//button[normalize-space()='Generate Invoice'][1]"
    _Tenant_name_dropdown = "//input[@autocomplete='off']"
    _select_tenant_dropdown_option = "//li[contains(@id,'option-0')]"
    _select_tenant_dropdown = "//*[@name='tenant_id']"
    _get_details_button = "//button[normalize-space()='Get Details']"
    _Cancel_button = "//button[normalize-space()='Cancel']"
    _generate_invoice_button = "//button[normalize-space()='Generate Invoice']"
    _download_invoice_button = "(//h6[@class='MuiTypography-root MuiTypography-h6 css-1loe7ol'])[6]"
    _calender_icon = "(//button[@aria-label='Choose date'])"
    _expand_year = ("//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium "
                    "MuiPickersCalendarHeader-switchViewIcon css-sldnni']")
    _select_past_year = "//button[normalize-space()='2023']"
    _select_year = "//button[normalize-space()='2025']"
    _select_from_date = "//button[normalize-space()='6']"
    _select_to_date = "//button[normalize-space()='29']"
    _select_due_date = "//button[normalize-space()='29']"
    _search_tenant = "//input[@placeholder='Search']"
    _invoice_generated_success = "//div[@id='notistack-snackbar']"

    def SearchTenant(self, data):
        self.element_click(self._search_tenant, "xpath")
        self.send_keys(data, self._search_tenant, "xpath")

    def clickongenerateinvoice(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._generateinvoice, "xpath")

    def entertenant(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._Tenant_name_dropdown, "xpath")
        self.send_keys('Tsstest', self._Tenant_name_dropdown, "xpath")

    def clickontenant(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._select_tenant_dropdown, locator_type="xpath")
        self.element_click(self._select_tenant_dropdown_option, locator_type="xpath")

    def selectfromdate(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._calender_icon, "xpath")
        self.wait_for_element(self._expand_year, "xpath")
        self.element_click(self._expand_year, "xpath")
        self.wait_for_element(self._select_past_year, "xpath")
        self.element_click(self._select_past_year, "xpath")
        self.wait_for_element(self._select_from_date, "xpath")
        self.element_click(self._select_from_date, "xpath")

    def selecttodate(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._calender_icon, "xpath")
        self.wait_for_element(self._expand_year, "xpath")
        self.element_click(self._expand_year, "xpath")
        self.wait_for_element(self._select_year, "xpath")
        self.element_click(self._select_year, "xpath")
        self.wait_for_element(self._select_to_date, "xpath")
        self.element_click(self._select_to_date, "xpath")

    def selectduedate(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.element_click(self._calender_icon, "xpath")
        self.wait_for_element(self._expand_year, "xpath")
        self.element_click(self._expand_year, "xpath")
        self.wait_for_element(self._select_year, "xpath")
        self.element_click(self._select_year, "xpath")
        self.wait_for_element(self._select_due_date, "xpath")
        self.element_click(self._select_due_date, "xpath")

    def clickongetdetails(self):
        time.sleep(5)
        self.element_click(self. _get_details_button, locator_type="xpath")

    def clickonGenerateInvoicebutton(self):
        self.wait_for_element(self._generate_invoice_button, locator_type="xpath")
        self.element_click(self._generate_invoice_button, locator_type="xpath")

    def downloadInvoice(self):
        self.wait_for_element(self._download_invoice_button, locator_type="xpath")
        self.element_click(self._download_invoice_button, locator_type="xpath")

    def verifygenerateinvoice(self):
        self.clickongenerateinvoice()
        self.entertenant()
        self.clickontenant()
        self.selectfromdate()
        self.selecttodate()
        self.selectduedate()
        self.clickongetdetails()
        time.sleep(5)
        self.clickonGenerateInvoicebutton()
        time.sleep(5)
        self.downloadInvoice()
        time.sleep(6)

    def verifyinvoicegeneration(self):
        self.verify_by_comparing_text(locator=self._invoice_generated_success, locator_type="xpath",
                                      expected_result=self.expected_result, result_msg="InvoiceTest")
