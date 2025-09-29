import time
import unittest
import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.UserManagement.UserGroups import UserGroups


@pytest.mark.usefixtures("tech_campus_setup")
class CreateUserGroup(unittest.TestCase):
    username = ReadConfig.get_hr_username()
    password = ReadConfig.get_hr_password()
    group_name = ReadConfig.getGroupName()
    group_desc = ReadConfig.getGroupDesc()
    editGDesc = ReadConfig.getEditedGDesc()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ug = UserGroups(self.driver)

    @pytest.mark.run()
    def test_UserGroups(self):
        self.cl.info("********** TestCase: HR - UserGroup **********")
        self.lp.login(self.username, self.password)
        self.ug.clickOnUserManagementOption()
        self.ug.createUserGroup(self.group_name, self.group_desc)
        time.sleep(1)
        self.ug.editUserGroup(self.editGDesc)
        time.sleep(1)
        self.ug.deleteUserGroup()
        time.sleep(2)

