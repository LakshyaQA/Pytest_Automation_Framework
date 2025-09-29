import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.ContentManagement.ViewButtons import ViewButtons


@pytest.mark.usefixtures("tech_campus_setup")
class ViewingButtons(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.vb = ViewButtons(self.driver)

    @pytest.mark.run()
    def test_ViewButtons(self):
        self.cl.info("*********** TestCase: HOD - Viewing Buttons **********")
        self.lp.login(self.username, self.password)
        self.vb.ViewingButtons()
