import time
import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.UserManagement.UserRoles import UserRoles


@pytest.mark.usefixtures("tech_campus_setup")
class CreatingUserRole(unittest.TestCase):
    username = ReadConfig.get_hr_username()
    password = ReadConfig.get_hr_password()
    role_name = ReadConfig.getRoleName()
    role_desc = ReadConfig.getRoleDesc()
    editRDesc = ReadConfig.getEditedRDesc()
    search_role = ReadConfig.getSearchRoleValue()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ur = UserRoles(self.driver)
        time.sleep(1)

    @pytest.mark.run()
    def test_UserRoles(self):
        self.cl.info("********** TestCase: HR - UserRole **********")
        self.lp.login(self.username, self.password)
        self.ur.clickOnUserManagementOption()
        self.ur.createUserRole(self.role_name, self.role_desc)
        time.sleep(1)
        self.ur.editTheUserRole(self.editRDesc)
        time.sleep(1)
        self.ur.deleteTheUserRole()
        time.sleep(1)
        self.ur.searchTheUserRole(self.search_role)


