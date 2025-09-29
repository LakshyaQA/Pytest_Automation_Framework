import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.MOOCCourses.AffiliateCourses import AffiliateCourses


@pytest.mark.usefixtures("tech_campus_setup")
class AffiliateCourse(unittest.TestCase):
    username = ReadConfig.get_Mooc_username()
    password = ReadConfig.get_Mooc_password()
    cost = ReadConfig.getCourseCost()
    credit_points = ReadConfig.getCourseCreditPoints()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ac = AffiliateCourses(self.driver)

    @pytest.mark.run()
    def test_AffiliateCourses(self):
        self.cl.info("********** TestCase: MOOCAdmin - AffiliateCourse **********")
        self.lp.login(self.username, self.password)
        self.ac.gotoMoocCoursesScreen()
        self.ac.AffiliateTheCourse(self.cost, self.credit_points)
        self.ac.verifying_AffiliateCourse()
