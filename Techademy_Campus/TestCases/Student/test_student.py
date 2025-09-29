import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.student import Student

import unittest
import pytest

@pytest.mark.usefixtures("tech_campus_setup")
class StudentTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.sd = Student(self.driver)






    @pytest.mark.run()
    def test_student(self):
        self.cl.info("************   TestCase  : Registrar Role : Student    ************")
        self.lp.login(self.username, self.password)
        self.sd.click_on_manage()
        self.sd.click_on_student()
        self.sd.click_onboard_student()
        self.sd.enter_mandatory_details()
        time.sleep(2)
        self.sd.search_student()
        time.sleep(2)
        self.sd.edit_student_details()
        time.sleep(2)
        self.sd.delete_student()
        time.sleep(2)




