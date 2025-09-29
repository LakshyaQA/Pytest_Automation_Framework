import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.NotificationPage import Notification


@pytest.mark.usefixtures("tech_one_setup")
class NotificationCreationTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.nc = Notification(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(24)
    def test_Notification_creation(self):
        self.cl.info("************  Test Case Started : Notification Creation Test  ************")
        self.lp.login(self.username, self.password)
        self.db.CloseChatBot()
        self.db.NavigateToNotificationTab()
        self.nc.create_notification()
        self.nc.verify_notification_creation()
