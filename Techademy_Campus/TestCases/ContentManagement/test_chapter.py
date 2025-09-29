import time
import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.Chapter import Chapter
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class AddEditDeleteChapter(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    chapter_name = ReadConfig.getChapterName()
    chapter_objective = ReadConfig.getChapterObjective()
    mm_dd_yyyy = ReadConfig.getDate()
    edited_objective = ReadConfig.getEditedObjective()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ac = Chapter(self.driver)

    @pytest.mark.run()
    def test_Chapter(self):
        self.cl.info("*********** TestCase: HOD - Chapter **********")
        self.lp.login(self.username, self.password)
        self.ac.adding_the_Chapter(self.chapter_name, self.chapter_objective)
        time.sleep(1)
        # self.ac.chapter_creation_verification()
        self.ac.editing_the_Chapter(self.edited_objective)
        time.sleep(1)
        # self.ac.edit_chapter_verification()
        self.ac.deleting_the_Chapter()
        time.sleep(1)
        # self.ac.delete_chapter_verification()
