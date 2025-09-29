import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.holiday import Holiday
import unittest
import pytest


@pytest.mark.usefixtures("tech_campus_setup")
class HolidayTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.hc = Holiday(self.driver)

    @pytest.mark.last
    def test_holiday(self):
        self.cl.info("************    TestCase : Registrar Role : Holiday      **********")
        self.lp.login(self.username, self.password)
        self.hc.create_holiday(" ")
        time.sleep(1)
        self.hc.update_holiday(" ")
        time.sleep(2)
        self.hc.delete_holiday()
        time.sleep(3)
        # self.hc.click_on_cancel_button()
