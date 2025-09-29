import time
import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.UserManagement.Users import Users


@pytest.mark.usefixtures("tech_campus_setup")
class CreatingUser(unittest.TestCase):
    username = ReadConfig.get_hr_username()
    password = ReadConfig.get_hr_password()
    f_name = ReadConfig.getFirstName()
    l_name = ReadConfig.getLastName()
    phone = ReadConfig.getMobileNumber()
    email = ReadConfig.getEmailID()
    search_user = ReadConfig.getSearchUserValue()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.cu = Users(self.driver)

    @pytest.mark.run()
    def test_Users(self):
        self.cl.info("********** TestCase: HR - Users **********")
        self.lp.login(self.username, self.password)
        self.cu.clickOnUserManagementOption()
        self.cu.create_user(self.f_name, self.l_name, self.phone, self.email)
        time.sleep(2)
        self.cu.searchTheUser(self.search_user)
        time.sleep(2)

