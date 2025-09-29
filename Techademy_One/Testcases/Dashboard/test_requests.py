import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.Requests import Requests
from Techademy_One.pageObject.TenantListPage import TenantList
from Techademy_One.pageObject.UserGroups import UserGroup
from Techademy_One.pageObject.UserManagementPage import UserManagement
from Techademy_One.pageObject.CreateTenantPage import TenantDetails


@pytest.mark.usefixtures("tech_one_setup")
class RequestTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.tm = TenantList(self.driver)
        self.um = UserManagement(self.driver)
        self.ug = UserGroup(self.driver)
        self.rq = Requests(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(35)
    def test_verify_if_superadmin_can_navigate_to_request_tab(self):
        self.cl.info("************  Test Case Started : Super Admin : Request Tab  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToRequestTab()
        self.rq.verify_requests()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(36)
    def test_verify_if_superadmin_can_navigate_to_request_info(self):
        self.cl.info("************  Test Case Started : Super Admin : Request Tab  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToRequestTab()
        self.rq.click_on_req_id()
        self.rq.verify_req_name()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(37)
    def test_verify_if_superadmin_can_navigate_to_pending_req(self):
        self.cl.info("************  Test Case Started : Super Admin : Request Tab  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToRequestTab()
        self.rq.click_on_pending()
        self.rq.verify_pending_tab()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(38)
    def test_verify_if_superadmin_can_navigate_to_completed_req(self):
        self.cl.info("************  Test Case Started : Super Admin : Request Tab  **********")
        self.lp.login(self.username, self.password)
        self.db.NavigateToRequestTab()
        self.rq.click_on_completed()
        self.rq.verify_completed_tab()

