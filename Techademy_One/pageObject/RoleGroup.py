"""
    This page includes locators and functions of role group page

    """

from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig


class RoleGroup(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'RoleGrp_creation')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_role_grp = "//input[@placeholder='Search Role Group']"
    _create_role_grp = "//button[normalize-space()='Create Role Groups']"  # On role group page as well as to save role grp
    _enter_role_grp_name = "//*[@name='group_name']"
    _expand_tech_role = "//td[text()='TECHADEMY ONE']/ancestor::tr//button[@aria-label='expand row']"
    _expand_courses_role = "//td[text()='LXP']/ancestor::tr//button[@aria-label='expand row']"
    _expand_labs_role = "//td[text()='LABS']/ancestor::tr//button[@aria-label='expand row']"
    _expand_assessment_role = "//td[text()='ASSESSMENT']/ancestor::tr//button[@aria-label='expand row']"
    _expand_hiring_role = "//td[text()='HIRING']/ancestor::tr//button[@aria-label='expand row']"
    _select_tenant_admin_labs = "//tr[contains(@class, 'MuiTableRow-root')]//td[contains(., 'tenantadmin')]//input[@type='checkbox']"
    _select_tenant_admin_tech = "//tr[contains(@class, 'MuiTableRow-root')]//td[contains(., 'tenantadmin')]//input[@type='checkbox']"
    _view_role_grp = "//*[@id='root']/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/a"
    _edit_rolegrp = "//img[@src='/main/editPurple.svg']"
    _delete_rolegrp = "//img[@src='/main/DeletePurple.svg']"
    _delete_confirm = "//button[normalize-space()='Yes, Delete']"
    _role_grp_success_msg = "//*[@id='notistack-snackbar' and contains(text(),'Details Saved Successfully')]"
    _save_role_group = "//button[normalize-space()='Create Role Group']"  # Create button on enter role group name page

    def SearchRole(self, role):
        self.wait_for_element(self._search_role_grp, locator_type="xpath")
        ele = self.get_element(self._search_role_grp, locator_type="xpath")
        ele.click()
        ele.send_keys(role)
        ele.send_keys(Keys.ENTER)

    def viewRole(self):
        self.element_click(self._view_role_grp, locator_type="xpath")

    def editRole(self):
        self.element_click(self._edit_rolegrp, locator_type="xpath")

    def deleteRole(self):
        self.element_click(self._delete_rolegrp, locator_type="xpath")
        self.wait_for_element(self._delete_confirm, "xpath")
        self.element_click(self._delete_confirm,"xpath")

    def clickOnCreateRole(self):
        self.element_click_js(self._create_role_grp, locator_type="xpath")

    def enterRoleName(self, name):
        self.send_keys(name, self._enter_role_grp_name, locator_type="xpath")

    def selectLabsRole(self):
        self.element_click(self._expand_labs_role, locator_type="xpath")
        self.wait_for_element(self._select_tenant_admin_labs, locator_type="xpath")
        self.element_click_js(self._select_tenant_admin_labs, locator_type="xpath")

    def selectTechRole(self):
        self.element_click(self._expand_tech_role, locator_type="xpath")
        self.web_scroll("down")
        self.wait_for_element(self._select_tenant_admin_tech, locator_type="xpath")
        self.element_click(self._select_tenant_admin_tech, locator_type="xpath")


    def clickOnSaveRole(self):
        self.element_click_js(self._save_role_group, locator_type="xpath")



    def CreateRoleGroup(self, name):
        self.clickOnCreateRole()
        self.enterRoleName(name)
        self.selectTechRole()
        self.clickOnSaveRole()

    def VerifyRoleGrpCreation(self,var):
        self.verify_by_comparing_text(locator="//h6[contains(text(),'"+var+"')]", locator_type="xpath",
                                      expected_result=var, result_msg="RoleGrpTest")



    def VerifyDeleteRoleGrp(self):
        self.verify_by_comparing_text("//*[@id='notistack-snackbar']","xpath","Role Group Deleted Successfully","RoleGrpdelete")