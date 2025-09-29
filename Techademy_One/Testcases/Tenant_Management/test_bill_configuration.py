import time
import unittest

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.Billing import BillingConfiguration
from Techademy_One.pageObject.BusinessUnit import BusinessUnit
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.RoleGroup import RoleGroup
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class BillConfigurationTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    tenant_name = TenantDetails.tenant_name


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.bl = BillingConfiguration(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(13)
    def test_configure_bill(self):
        self.cl.info("**********  Test Case Started : Bill Configuration by Superadmin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToBilling(self.tenant_name)
        self.bl.SetBillParameters()
        self.bl.verifyBillConfiguration()