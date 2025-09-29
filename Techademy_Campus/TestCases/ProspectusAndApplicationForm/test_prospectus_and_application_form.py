# import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.prospectusAndApplicationForm import ProspectusAndApplicationForm
import unittest
import pytest

@pytest.mark.usefixtures("tech_campus_setup")
class ProspectusAndApplicationFormTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.pf = ProspectusAndApplicationForm(self.driver)


    def test_prospectus_and_application_form(self):
        self.cl.info("************  TestCase: Registrar Role : Prospectus And Application Form    **********")
        self.lp.login(self.username, self.password)
        # self.pf.search()
        # time.sleep(1)
        self.pf.creation_prospectus_and_application_form()
        # time.sleep(3)
