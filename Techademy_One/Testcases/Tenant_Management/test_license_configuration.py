import time
import unittest

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.Billing import BillingConfiguration
from Techademy_One.pageObject.BusinessUnit import BusinessUnit
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.Licensing import Licensing
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.RoleGroup import RoleGroup
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class LicenseConfigurationTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    tenant_name = TenantDetails.tenant_name



    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.sd = SeleniumDriver(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.lc = Licensing(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(14)
    def test_generate_license(self):
        self.cl.info("**********  Test Case Started : License Configuration by Superadmin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToLicense(self.tenant_name)
        self.lc.LicenseConfigure()
        self.lc.verifyLicensing()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(15)
    def test_activate_license(self):
        self.cl.info("**********  Test Case Started : Activate License by Superadmin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToLicense(self.tenant_name)
        self.lc.ActivateLicense()
        self.lc.verifyActivateLicense()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(16)
    def test_view_license(self):
        self.cl.info("**********  Test Case Started : View License by Superadmin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToLicense(self.tenant_name)
        self.lc.clickOnViewLicense()
        self.lc.verifyViewLicense()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(43)
    def test_generate_license_when_there_is_already_active_license(self):
        self.cl.info("**********  Test Case Started : License Configuration by Superadmin **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToTenantTab()
        self.tm.NavigateToLicense(self.tenant_name)
        self.lc.LicenseConfigure()
        self.lc.verifyLicenseAlreadyexists()