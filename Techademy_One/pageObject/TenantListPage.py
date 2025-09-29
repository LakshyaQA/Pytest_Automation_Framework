"""
    This page includes locators and functions of tenant list page where list of all tenants is displayed

    """

import time

import allure
from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


class TenantList(Basepage):
    delete_expected_result = ReadConfig.get_expected_result('Expected Results', 'delete_tenant_msg')
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _create_tenant_button = "//button[normalize-space()='Create Tenant']"
    _search_button = "//input[@placeholder='Search Tenant']"
    _tenant_view = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1loe7ol']"
    _tenant_menu = "//img[@src='/main/ico-more_vert.svg']"
    _click_activate = "//h6[normalize-space()='Activate']"
    _activate_popup_up = "//button[normalize-space()='Yes, Activate']"
    _create_tenant_header = "//*[@class='MuiTypography-root MuiTypography-h3 css-kkhisd']"
    _edit_tenant = "//img[@src ='main/EditIcon.svg']"
    _delete_tenant = "//img[@src ='/main/DeleteIcon.svg']"
    _Yes_delete = "//button[normalize-space()='Yes, Delete']"
    _basic_details = "//button[normalize-space()='Basic Details']"
    _customize_tab = "//button[normalize-space()='Customizations']"
    _Plan_tab = "//button[normalize-space()='Plan Details']"
    _Config_tab = "//button[normalize-space()='Configurations']"
    _role_grp_tab = "//button[normalize-space()='Role Group']"
    _business_uni_tab = "//button[normalize-space()='Business Units']"
    _users_tab = "//button[normalize-space()='Users']"
    _licensing_tab = "//button[normalize-space()='License']"
    _billing_tab = "//button[normalize-space()='Billing']"
    _tenant_delete_msg = "//*[@id='notistack-snackbar' and contains(text(),'Tenant Deleted Successfully')]"
    tenant_name = TenantDetails.tenant_name

    def ClickonCreate(self):

        self.element_click_js(self._create_tenant_button, locator_type="xpath")

    def SearchTenant(self, tenant_name):
        ele = self.get_element(self._search_button, locator_type="xpath")
        self.wait_for_element(ele)
        ele.click()
        ele.send_keys(tenant_name)
        ele.send_keys(Keys.ENTER)
        time.sleep(5)

    def ClickonViewTenant(self, tenant_name):
        self.SearchTenant(tenant_name)
        self.element_click_js(self._tenant_view, locator_type="xpath")

    def ClickonActivate(self):
        self.element_click_js(self._click_activate, locator_type="xpath")

    def clickOnConfirmation(self):
        self.element_click(self._activate_popup_up, locator_type="xpath")

    def ClickonTenantMenu(self):
        self.element_click_js(self._tenant_menu, locator_type="xpath")

    def ClickOnEdit(self):
        self.element_click(self._edit_tenant, locator_type="xpath")

    def ClickOnDelete(self):
        self.element_click_js(self._delete_tenant, locator_type="xpath")

    def ClickOnDeleteConfirmation(self):
        self.wait_till_element_invisibility("//div[@class='loading']","xpath")
        self.element_click(self._Yes_delete, "xpath")

    def ClickOnBusinessUnit(self):
        self.element_click_js(self._business_uni_tab, locator_type="xpath")

    def ClickonBasicDetailsTab(self):
        self.element_click(self._basic_details, locator_type="xpath")

    def ClickonCustomize(self):
        self.element_click(self._customize_tab, locator_type="xpath")

    def ClickOnPlanDetails(self):
        self.element_click(self._Plan_tab, locator_type="xpath")

    def ClickOnUsers(self):
        self.element_click_js(self._users_tab, locator_type="xpath")

    def ClickOnRoleGrp(self):
        self.element_click_js(self._role_grp_tab, locator_type="xpath")

    def ClickOnConfig(self):
        self.element_click(self._Config_tab, locator_type="xpath")

    def ClickOnLicense(self):
        self.element_click(self._licensing_tab,"xpath")

    def ClickOnBilling(self):
        self.wait_till_element_invisibility("//div[@class='loading']","xpath")
        self.wait_for_element(self._billing_tab, "xpath")
        self.element_click(self._billing_tab,"xpath")

    def DeleteTenant(self):
        time.sleep(5)
        self.ClickonTenantMenu()
        self.ClickOnDelete()
        time.sleep(5)
        self.ClickOnDeleteConfirmation()

    def NavigateToBasicDetails(self, name):
        self.ClickonViewTenant(name)
        self.ClickonBasicDetailsTab()

    def NavigateToCustomize(self, name):
        self.ClickonViewTenant(name)
        self.ClickonCustomize()

    def NavigateToPlan(self, name):
        self.ClickonViewTenant(name)
        self.wait_till_element_invisibility("//div[@class='loading']","xpath")
        self.ClickOnPlanDetails()

    def NavigateToConfig(self, name):
        self.ClickonViewTenant(name)
        self.ClickOnConfig()

    def NavigateToRoleGroup(self, name):
        self.ClickonViewTenant(name)
        time.sleep(2)
        self.ClickOnRoleGrp()

    def NavigateToBU(self, name):
        self.ClickonViewTenant(name)
        self.ClickOnBusinessUnit()

    def NavigateToUsers(self, name):
        self.ClickonViewTenant(name)
        self.ClickOnUsers()

    def NavigateToLicense(self, name):
        self.ClickonViewTenant(name)
        self.wait_till_element_invisibility("//div[@class='loading']","xpath")
        self.ClickOnLicense()

    def NavigateToBilling(self, name):
        self.ClickonViewTenant(name)
        self.ClickOnBilling()



    def VerifyCreateTen(self):
        self.verify_by_element_presence(locator=self._create_tenant_header, locator_type="xpath", result_msg="CreateTenantButton")

    def VerifyMenuClick(self):
        self.verify_by_element_presence(locator=self._edit_tenant,locator_type="xpath",result_msg="MenuClickTest")


    def VerifyTenantDetails(self):
        self.verify_by_element_presence(locator=self._basic_details,locator_type="xpath",result_msg="ViewTenantTest")


    def VerifySearchTenant(self):
        self.verify_by_element_presence(locator=self._tenant_view,locator_type="xpath",result_msg="SearchTenantTest")


    def VerifyTenantdeletion(self):
        self.verify_by_comparing_text(locator=self._tenant_delete_msg, locator_type="xpath",
                                      expected_result=self.delete_expected_result, result_msg="TenantDeleteTest")

    def verifyActivateTenant(self):
        self.verify_by_comparing_text("(//h6[@class='MuiTypography-root MuiTypography-h6 css-1loe7ol'])[2]","xpath","Active","ActivateTest")