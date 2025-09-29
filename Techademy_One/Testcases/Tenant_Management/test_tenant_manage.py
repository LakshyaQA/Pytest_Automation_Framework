import time
import unittest

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.BusinessUnit import BusinessUnit
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.RoleGroup import RoleGroup
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class TenantManageTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    tenant_name = TenantDetails.tenant_name
    bu_name = ReadConfig.get_bu_name('Business Unit', 'Bu_name')
    bu_desc = ReadConfig.get_bu_desc()
    role_grp = ReadConfig.get_role_grp()
    role_group_name = ReadConfig.get_role_grp_name('Role Group', 'role_grp_name')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.bu = BusinessUnit(self.driver)
        self.rg = RoleGroup(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(8)
    def test_tenant_activation(self):
        self.cl.info("**********  Test Case Started : Activate Tenant **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonManage()
        self.db.ClickonTenant()
        self.tm.SearchTenant(self.tenant_name)
        self.tm.ClickonActivate()
        self.tm.clickOnConfirmation()
        self.tm.verifyActivateTenant()
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(9)
    def test_search_tenant(self):
        self.cl.info("*********** Test Case Started : Search Tenant  ***********")
        self.lp.login(self.username, self.password)
        self.db.ClickonManage()
        self.db.ClickonTenant()
        self.tm.SearchTenant(self.tenant_name)
        self.tm.VerifySearchTenant()
        time.sleep(2)

        # result = self.db.VerifyManageTest()
        # self.ts.markFinal("test_manage", result,"Test Done")

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(10)
    def test_view_tenant(self):
        self.cl.info("***********  Test Case Started : View Tenant  ***********")
        self.lp.login(self.username, self.password)
        self.db.ClickonManage()
        self.db.ClickonTenant()
        self.tm.ClickonViewTenant(self.tenant_name)
        self.tm.VerifyTenantDetails()
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(12)
    def test_BusinessUnit_creation_for_superadmin(self):
        self.cl.info("**********  Test Case Started : Create Business Unit  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToBU(self.tenant_name)
        self.bu.CreateBusinessUnit(self.bu_name, self.bu_desc)
        self.bu.VerifyBUCreation()
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(11)
    def test_rolegrp_creation_for_superadmin(self):
        self.cl.info("************  Test Case Started : Create Role Group  ************")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToRoleGroup(self.tenant_name)
        self.rg.CreateRoleGroup(self.role_group_name)
        self.rg.VerifyRoleGrpCreation(self.role_group_name)
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(44)
    def test_tenant_deletion(self):
        self.cl.info("************ Test Case Started : Delete Tenant **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.SearchTenant(self.tenant_name)
        self.tm.DeleteTenant()
        self.tm.VerifyTenantdeletion()




