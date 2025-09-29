import time
import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.UserManagement.ImportUser import ImportUser


@pytest.mark.usefixtures("tech_campus_setup")
class ImportUsers(unittest.TestCase):
    username = ReadConfig.get_hr_username()
    password = ReadConfig.get_hr_password()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.iu = ImportUser(self.driver)
        time.sleep(1)

    @pytest.mark.run()
    def test_importUsers(self):
        self.cl.info("********** TestCase: HR - ImportUsers **********")
        self.lp.login(self.username, self.password)
        self.iu.clickOnUserManagementOption()
        self.iu.importTheUsers()
        time.sleep(2)
