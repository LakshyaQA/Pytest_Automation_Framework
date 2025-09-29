import time
import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.BusinessUnit import BusinessUnit
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.Licensing import Licensing
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.RoleGroup import RoleGroup
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class TenantManageAdminTests(unittest.TestCase):
    username = ReadConfig.get_username('tenant admin', 'tenantusername1')
    password = ReadConfig.get_password('tenant admin', 'tenantpassword1')
    bu_name = ReadConfig.get_bu_name('Business Unit', 'Bu_name1')
    bu_desc = ReadConfig.get_bu_desc()
    role_grp = ReadConfig.get_role_grp()
    role_group_name = ReadConfig.get_role_grp_name('Role Group', 'role_grp_name1')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.rg = RoleGroup(self.driver)
        self.bu = BusinessUnit(self.driver)
        self.lc = Licensing(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(19)
    def test_tenant_details(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Tenant details  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTabAdmin()
        self.tm.VerifyTenantDetails()
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(21)
    def test_Business_unit_creation_for_admin(self):
        self.lp.login(self.username, self.password)
        self.cl.info("************  Test Case Started : Tenant Admin : Create BU  **********")
        self.db.NavigateToTenantTabAdmin()
        self.tm.ClickOnBusinessUnit()
        self.bu.CreateBusinessUnit(self.bu_name, self.bu_desc)
        self.bu.VerifyBUCreation()
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(20)
    def test_role_grp_creation_for_admin(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Create Role Group  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTabAdmin()
        self.tm.ClickOnRoleGrp()
        self.rg.CreateRoleGroup(self.role_group_name)
        self.rg.VerifyRoleGrpCreation(self.role_group_name)
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(31)
    def test_role_grp_deletion(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Create Role Group  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTabAdmin()
        self.tm.ClickOnRoleGrp()
        self.rg.deleteRole()
        self.rg.VerifyDeleteRoleGrp()
        time.sleep(2)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(22)
    def test_view_license_for_admin(self):
        self.lp.login(self.username, self.password)
        self.cl.info("************  Test Case Started : Tenant Admin : View License  **********")
        self.db.NavigateToTenantTabAdmin()
        self.tm.ClickOnLicense()
        self.lc.clickOnViewLicense()
        self.lc.verifyViewLicense()
        time.sleep(2)
