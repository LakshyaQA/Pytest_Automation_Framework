import time
import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.DiscussionBoard import DiscussionBoard
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class CreateDiscussionBoard(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    title = ReadConfig.getDiscussionTitle()
    desc = ReadConfig.getDiscussionDesc()
    poll_one = ReadConfig.getPollOneOption()
    poll_two = ReadConfig.getPollTwoOption()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.db = DiscussionBoard(self.driver)
        time.sleep(2)

    @pytest.mark.run()
    def test_create_discussion(self):
        self.cl.info("*********** TestCase - CreatingDiscussion **********")
        self.lp.login(self.username, self.password)
        self.db.clickOnDiscussionBoardOption()
        self.db.createDiscussion(self.title, self.desc, self.poll_one, self.poll_two)
        time.sleep(2)
        self.db.discussion_creation_verification()
        self.cl.log("Passed")
