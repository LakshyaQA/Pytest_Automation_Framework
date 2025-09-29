# import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.universityMission import UniversityMission
import unittest
import pytest

@pytest.mark.usefixtures("tech_campus_setup")
class UniversityMissionTest(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.um = UniversityMission(self.driver)

    def test_university_Mission(self):
        self.cl.info("************TestCase : Registrar Role : University Mission  **********")
        self.lp.login(self.username, self.password)
        self.um.create_university_mission()
        self.um.preview_university_mission()

