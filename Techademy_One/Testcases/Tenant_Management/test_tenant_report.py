import time
import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.ReportsPage import Report

@pytest.mark.usefixtures("tech_one_setup")
class ReportAdminTests(unittest.TestCase):
    username = ReadConfig.get_username('tenant admin', 'tenantusername1')
    password = ReadConfig.get_password('tenant admin', 'tenantpassword1')
    report = ReadConfig.get_Report_name(section='Report', opt='report_name')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.rp = Report(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(40)
    def test_report_tab(self):
        self.cl.info("************  Test Case Started : Tenantadmin : Reports **********")
        self.lp.login(self.username, self.password)
        time.sleep(2)
        self.db.ClickontenantReport()
        self.rp.ReportGenerationTenant(self.report)
        self.rp.VerifyReportGenerationTenant()
