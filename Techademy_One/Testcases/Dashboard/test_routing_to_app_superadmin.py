import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_one_setup", "set_up")
class RoutingTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(3)
    def test_verify_if_superadmin_can_route_to_MML(self):
        self.cl.info("************  Test Case Started : Super Admin : Route_To_Labs  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToLabs()
        self.db.Verify_MML()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(4)
    def test_verify_if_superadmin_can_route_to_assessments(self):
        self.cl.info("************  Test Case Started : Super Admin : Route_To_Assessments  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToAssessments()
        self.db.Verify_Yaksha()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(5)
    def test_verify_if_superadmin_can_route_to_LXP(self):
        self.cl.info("************  Test Case Started : Super Admin : Route_To_LXP  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToLXP()
        self.db.Verify_LXP()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(6)
    def test_verify_if_superadmin_can_route_to_Hiring(self):
        self.cl.info("************  Test Case Started : Super Admin : Route_To_ReCrewt  **********")
        self.lp.login(self.username, self.password)
        self.db.navigateToRecrewt()
        self.db.Verify_Recrewt()
