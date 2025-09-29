import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.CreatePeerGroupInteraction import CreateInteraction
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class CreatingInteraction(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    title = ReadConfig.getInteractionTitle()
    desc = ReadConfig.getInteractionDesc()
    poll_one = ReadConfig.getPollOneOption()
    poll_two = ReadConfig.getPollTwoOption()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ci = CreateInteraction(self.driver)

    @pytest.mark.run()
    def test_CreatePeerGroupInteraction(self):
        self.cl.info("********** TestCase: HOD - CreatePeerGroupInteraction **********")
        self.lp.login(self.username, self.password)
        self.ci.createInteraction(self.title, self.desc, self.poll_one, self.poll_two)
