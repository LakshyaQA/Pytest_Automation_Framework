import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.AddVideoLink import AddVideoLink
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class AddingVideoLink(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    AddVideo_title = ReadConfig.getAddVideoTitle()
    AddVideo_link = ReadConfig.getAddVideoLink()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.vl = AddVideoLink(self.driver)

    @pytest.mark.run()
    def test_AddVideoLink(self):
        self.cl.info("********** TestCase: HOD - AddVideoLink **********")
        self.lp.login(self.username, self.password)
        self.vl.addingTheVideoLink(self.AddVideo_title, self.AddVideo_link)
