import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.AddReading import AddReading
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class AddReadings(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    reading_title = ReadConfig.getReadingTitle()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ar = AddReading(self.driver)

    @pytest.mark.run()
    def test_AddReadings(self):
        self.cl.info("********** TestCase: HOD - AddReadings **********")
        self.lp.login(self.username, self.password)
        self.ar.addingTheReadingFile(self.reading_title)
