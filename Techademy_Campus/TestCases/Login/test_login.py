import unittest
import time
import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class LoginTest(unittest.TestCase):
    username = ReadConfig.get_reg_username()
    password = ReadConfig.get_reg_password()
    # username = ReadConfig.get_HOD_username()
    # password = ReadConfig.get_HOD_password()
    # username = ReadConfig.get_Fac_username()
    # password = ReadConfig.get_Fac_password()
    # username = ReadConfig.get_Stud_username()
    # password = ReadConfig.get_Stud_password()
    # username = ReadConfig.get_HR_username()
    # password = ReadConfig.get_HR_password()
    # username = ReadConfig.get_Mooc_username()
    # password = ReadConfig.get_Mooc_password()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()

    @pytest.mark.run()
    def test_validLogin(self):
        self.cl.info("************ TestCase - Login into the Portal **********")
        self.lp.login(self.username, self.password)
        time.sleep(3)
