
import time
import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.ReportSettings import ReportSettingsTests


@pytest.mark.usefixtures("tech_one_setup")
class ReportSetting(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.rs = ReportSettingsTests(self.driver)


    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(39)
    def test_report_Settings(self):
        self.cl.info("************  Test Case Started : Super admin : Reports Settings **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonManage()
        self.db.ClickonReporting()
        time.sleep(3)
        self.rs.ReportSettings()
        self.rs.VerifyReportSettings()




