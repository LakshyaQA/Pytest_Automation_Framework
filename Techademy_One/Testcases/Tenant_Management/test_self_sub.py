import time
import unittest

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.Billing import BillingConfiguration
from Techademy_One.pageObject.BusinessUnit import BusinessUnit
from Techademy_One.pageObject.Custom_Plan import CustomPlan
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.Licensing import Licensing
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.RoleGroup import RoleGroup
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class SelfSubscriptionTest(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    username1 = ReadConfig.get_username('tenant admin', 'tenantusername1')
    password1 = ReadConfig.get_password('tenant admin', 'tenantpassword1')
    tenant_name = TenantDetails.tenant_name



    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.sd = SeleniumDriver(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.cp = CustomPlan(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(29)
    def test_default_plan_creation(self):
        self.cl.info("**********  Test Case Started : Default Plan Creation by Superadmin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToPlan(self.tenant_name)
        self.cp.CreateDefaultPlan("Default Plan","This is Default Plan")
        self.cp.verifyPlanCreation()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(30)
    def test_plan_details(self):
        self.cl.info("**********  Test Case Started : Custom Plan Creation by tenant admin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToPlan(self.tenant_name)
        self.cp.clickOnCheckPlanDetails()
        self.cp.verifyCheckDetails()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(33)
    def test_superadmin_can_activate_plan(self):
        self.cl.info("**********  Test Case Started : Custom Plan Creation by tenant admin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToPlan(self.tenant_name)
        self.cp.clickOnCheckPlanDetails()
        self.cp.clickOnActivatePlan()
        self.cp.verifyPlanActivation()

    # @pytest.mark.order(34)
    # def test_verify_if_tenant_admin_can_create_custom_plan(self):
    #     self.cl.info("**********  Test Case Started : Custom Plan Creation by tenant admin **********")
    #     self.lp.login(self.username1, self.password1)
    #     self.db.NavigateToTenantTabAdmin()
    #     self.tm.ClickOnPlanDetails()
    #     self.cp.CreateCustomPlan("Custom plan", "This is custom plan")
    #     self.cp.verifyPlanCreation()




