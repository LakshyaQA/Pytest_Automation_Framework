from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.universityVision import UniversityVision
import unittest
import pytest

@pytest.mark.usefixtures("tech_campus_setup")
class UniversityVisionTest(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.uv = UniversityVision(self.driver)

    def test_university_vision(self):
        self.cl.info("************ TestCase: Registrar Role : University vision  **********")
        self.lp.login(self.username, self.password)
        self.uv.create_university_vision()
        self.uv.preview_university_vision()
