import time
import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.StudentConnect import StudentConnect


@pytest.mark.usefixtures("tech_campus_setup")
class StudentConnection(unittest.TestCase):
    username = ReadConfig.get_HOD_username()
    password = ReadConfig.get_HOD_password()
    title = ReadConfig.get_SC_Title()
    description = ReadConfig.get_SC_Description()
    search_student = ReadConfig.get_search_student()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.sc = StudentConnect(self.driver)
        time.sleep(1)

    @pytest.mark.run()
    def test_StudentConnect(self):
        self.cl.info("********** TestCase: HOD - StudentConnection **********")
        self.lp.login(self.username, self.password)
        self.sc.StudentConnection(self.title, self.description)
        time.sleep(1)
        self.sc.SearchStudent(self.search_student)
        time.sleep(1)
        self.sc.DeleteStudentConnection()
        time.sleep(1)
