import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class DashboardTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    tenant_name = TenantDetails.tenant_name

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(2)
    def test_verify_manage_tab_is_clickable(self):
        self.cl.info("************  Test Case Started : Superadmin : Dashboard  **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonManage()
        self.db.ClickonTenant()
        self.db.VerifyTenantManage()
