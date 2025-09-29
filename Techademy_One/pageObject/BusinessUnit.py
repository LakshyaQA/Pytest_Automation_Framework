"""
    This page includes locators and functions of Business unit page

    """
import time

import allure
from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig


class BusinessUnit(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'Bu_creation')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_business_unit = "//input[@placeholder='Search Business Unit']"
    _add_BU = "//button[normalize-space()='Add Business Unit']"
    _enter_BU_name = "//*[@name='name']"
    _enter_BU_Desc = "//*[@name='description']"
    _select_rg = "//div[@name='group_id']"
    _submit_button = "//button[contains(text(),'Create Business Unit')]"
    _rg_option = "//li[contains(@id,'option-0')]"
    _BU_success = "//*[@id='notistack-snackbar']"

    def SearchBU(self, bu):
        self.wait_for_element(self._search_business_unit, locator_type="xpath")
        ele = self.get_element(self._search_business_unit, locator_type="xpath")
        ele.click()
        ele.send_keys(bu)
        ele.send_keys(Keys.ENTER)

    def ClickOnAddBU(self):
        self.element_click_js(self._add_BU, locator_type="xpath")

    def enterBUName(self, name):
        role_name = self.generate_random_name(name)
        self.send_keys(role_name, self._enter_BU_name, locator_type="xpath")

    def enterDesc(self, desc):
        self.send_keys(desc, self._enter_BU_Desc, locator_type="xpath")

    def selectRoleGrp(self):
        self.select_element(self._select_rg, self._rg_option,locator_type="xpath")

    def clickSubmit(self):
        self.element_click_js(self._submit_button, locator_type="xpath")

    def CreateBusinessUnit(self, name, dec):
        time.sleep(5)
        self.ClickOnAddBU()
        self.enterBUName(name)
        self.enterDesc(dec)
        self.selectRoleGrp()
        self.clickSubmit()

    def VerifyBUCreation(self):
        self.verify_by_comparing_text(locator=self._BU_success, locator_type="xpath",expected_result=self.expected_result,result_msg="BUCreationTest")

