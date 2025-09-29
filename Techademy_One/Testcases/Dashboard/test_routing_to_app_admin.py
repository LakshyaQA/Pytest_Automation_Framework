import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_one_setup", "set_up")
class RoutingTestsAdmin(unittest.TestCase):
    username = ReadConfig.get_username('tenant admin', 'tenantusername1')
    password = ReadConfig.get_password('tenant admin', 'tenantpassword1')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(23)
    def test_verify_if_tenantadmin_can_route_to_MML(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Route_To_MML  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToLabs()
        self.db.Verify_MML()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(24)
    def test_verify_if_tenantadmin_can_route_to_assessments(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Route_To_Yaksha  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToAssessments()
        self.db.Verify_Yaksha()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(25)
    def test_verify_if_tenantadmin_can_route_to_LXP(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Route_To_LXP  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToLXP()
        self.db.Verify_LXP()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(26)
    def test_verify_if_tenantadmin_can_route_to_Hiring(self):
        self.cl.info("************  Test Case Started : Tenant Admin : Route_To_Recrewt  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToRecrewt()
        self.db.Verify_Recrewt()
