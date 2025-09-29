"""
    This page includes locators and functions of User Group page

    """
import allure

import Common_Packages.Utility.custom_logger as cl

from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


class UserGroup(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'user_grp')
    grp_name1 = ReadConfig.get_grp_name('User Group', 'grp_name')
    desc = ReadConfig.get_grp_desc('User Group', 'desc')
    grp_name = SeleniumDriver.generate_random_name(grp_name1)
    grp_desc = SeleniumDriver.generate_random_name(desc)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_user_grp = "//input[@placeholder='Search User Group']"
    _create_user_grp = "//button[normalize-space()='Create User Groups']"
    _view_user_grp = "(//*[@class='MuiTypography-root MuiTypography-h6 css-1loe7ol'])[1]"
    _edit_user_grp = "(//img[@src='/main/editPurple.svg'])[1]"
    _delete_user_grp = "(//img[@src='/main/DeletePurple.svg'])[1]"
    _user_grp_name = "//*[@name='name']"
    _description = "//*[@name='description']"
    _select_tenant_dropdown = "//*[@name='tenant_id']"
    _tenant_dropdown_option = "//li[contains(@id,'option-0')]"
    _assign_user_dropdown_option = "//li[contains(@id,'option-0')]"
    _assign_user_dropdown = "//*[@name='user_details']"
    _cancel_btn = "//button[normalize-space()='Cancel']"
    _create_btn = "//button[normalize-space()='Create User Group']"
    _user_grp_creation_msg = "//div[@id='notistack-snackbar']"

    def SearchUser(self, data):
        self.element_click(self._search_user_grp, "xpath")
        self.send_keys(data, self._search_user_grp, "xpath")

    def clickCreateUserGrp(self):
        self.element_click_js(self._create_user_grp, "xpath")

    def clickViewUserGrp(self):
        self.element_click_js(self._view_user_grp, "xpath")

    def clickDeleteUserGrp(self):
        self.element_click_js(self._delete_user_grp, "xpath")

    def clickEditUserGrp(self):
        self.element_click_js(self._edit_user_grp, "xpath")

    def enterUserGrpName(self, name):
        self.element_click_js(self._user_grp_name, "xpath")
        self.send_keys(name, self._user_grp_name, "xpath")

    def enterUserGrpDesc(self, desc):
        self.element_click_js(self._description, "xpath")
        self.send_keys(desc, self._description, "xpath")

    def selectTenant(self):
        self.select_element(self._select_tenant_dropdown, self._tenant_dropdown_option, "xpath")

    def assignUsers(self):
        self.select_element(self._assign_user_dropdown, self._assign_user_dropdown_option, "xpath")

    def clickOnCreateBtn(self):
        self.element_click_js(self._create_btn, "xpath")

    def clickOnCancel(self):
        self.element_click(self._cancel_btn, "xpath")

    def CreateUserGroup(self,grp_name,desc):
        self.clickCreateUserGrp()
        self.enterUserGrpName(grp_name)
        self.enterUserGrpDesc(desc)
        self.selectTenant()
        self.assignUsers()
        self.clickOnCreateBtn()

    def create_usergroup_tenantadmin(self):
        self.clickCreateUserGrp()
        self.enterUserGrpName(self.grp_name)
        self.enterUserGrpDesc(self.grp_desc)
        self.assignUsers()
        self.clickOnCreateBtn()

    def VerifyUserGrpCreation(self):
        self.verify_by_comparing_text(locator=self._user_grp_creation_msg, locator_type="xpath",
                                      expected_result=self.expected_result, result_msg="UserGroupCreationTest")

