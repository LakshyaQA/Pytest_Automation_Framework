import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.DashboardPage import Dashboard
from Techademy_One.pageObject.LoginPage import LoginPage
from Techademy_One.pageObject.AuditLogsPage import AuditLogs


@pytest.mark.usefixtures("tech_one_setup")
class AuditLogTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')
    start_date = ReadConfig.get_start_date()
    end_date = ReadConfig.get_end_date()
    user_name = ReadConfig.get_username('Audit Logs', 'user_name')

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = Dashboard(self.driver)
        self.ag = AuditLogs(self.driver)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(33)
    def test_verify_if_superadmin_can_verify_ProductLogs(self):
        self.cl.info("************ Test Case Started : Audit Logs **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonAuditLogs()
        self.ag.VerifyAllProductLogs()
        self.ag.verifyLogs()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(34)
    def test_verify_if_superadmin_can_apply_Filter(self):
        self.cl.info("************ Test Case Started : Audit Logs **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonAuditLogs()
        self.ag.VerifyApplyFilter()
        self.ag.verifyLogs()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(35)
    def test_verify_if_superadmin_can_export_AuditLogs(self):
        self.cl.info("************ Test Case Started : Audit Logs **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonAuditLogs()
        self.ag.VerifyExport()
        self.ag.verifyLogs()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(36)
    def test_verify_if_superadmin_can_search_Users(self):
        self.cl.info("************ Test Case Started : Audit Logs **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonAuditLogs()
        self.ag.VerifySearch()
        self.ag.verifyLogs()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(37)
    def test_verify_Filter_Negative1(self):
        self.cl.info("************ Test Case Started : Audit Logs **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonAuditLogs()
        self.ag.clickOnFilterbutton()
        self.ag.clickOnApplyFilter()
        self.ag.VerifyApplyFilterNegative1()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(38)
    def test_verify_Filter_Negative2(self):
        self.cl.info("************ Test Case Started : Audit Logs **********")
        self.lp.login(self.username, self.password)
        self.db.ClickonAuditLogs()
        self.ag.ApplyFilterNegative()
        self.ag.VerifyApplyFilterNegative2()
