import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.MOOCCourses.PublishCourses import PublishCourses


@pytest.mark.usefixtures("tech_campus_setup")
class PublishCourse(unittest.TestCase):
    username = ReadConfig.get_Mooc_username()
    password = ReadConfig.get_Mooc_password()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.pc = PublishCourses(self.driver)

    @pytest.mark.run()
    def test_PublishCourses(self):
        self.cl.info("********** TestCase: MOOCAdmin - PublishCourse **********")
        self.lp.login(self.username, self.password)
        self.pc.gotoMoocCoursesScreen()
        self.pc.PublishTheCourse()
        self.pc.verifying_PublishCourses()
