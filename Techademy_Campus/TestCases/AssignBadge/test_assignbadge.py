# import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage

from Techademy_Campus.PageObject.assignBadge import AssignBadge
import unittest
import pytest


@pytest.mark.usefixtures("tech_campus_setup")
class AssignBadgeTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ab = AssignBadge(self.driver)

    @pytest.mark.last
    def test_assign_badge(self):
        self.cl.info("************   TestCase : Registrar Role : Assign Badge     **********")
        self.lp.login(self.username, self.password)
        self.ab.navigate_to_manage_tab()
        self.ab.verify_assigning_badge()


