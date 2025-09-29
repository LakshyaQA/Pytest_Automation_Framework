import time
import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.ReportsPage import Report


@pytest.mark.usefixtures("tech_one_setup")
class ReportsTest(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username1')
    password = ReadConfig.get_password('common info', 'password1')
    report = ReadConfig.get_Report_name(section='Report', opt='report_name')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.rp = Report(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(32)
    def test_report_generation(self):
        self.cl.info("************  Test Case Started : Superadmin : Reports **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonReports()
        self.rp.ReportGeneration(self.report)
        self.rp.verifyEmailNotification()
        self.rp.VerifyReportGeneration()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(33)
    def test_report_generation_Negative1(self):
        self.cl.info("************  Test Case Started : Superadmin : Reports **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonReports()
        self.rp.ReportGenerationNegative1(self.report)
        self.rp.VerifyReportGenerationError1()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(34)
    def test_report_generation_Negative2(self):
        self.cl.info("************  Test Case Started : Superadmin : Reports **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonReports()
        self.rp.ReportGenerationNegative2(self.report)
        self.rp.VerifyReportGenerationError2()
