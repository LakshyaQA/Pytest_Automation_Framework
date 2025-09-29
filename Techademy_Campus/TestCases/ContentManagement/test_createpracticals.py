import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.CreatePracticals import CreatePracticals
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class CreatingPracticals(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    practical_title = ReadConfig.getPhysicalPracticalTitle()
    practical_description = ReadConfig.getPhysicalPracticalDescription()
    start_time = ReadConfig.getPracticalStartTime()
    end_time = ReadConfig.getPracticalEndTime()
    location = ReadConfig.getPracticalLocation()
    VLab_title = ReadConfig.getVLabTitle()
    VLab_description = ReadConfig.getVLabDescription()
    VLab_stime = ReadConfig.getVLabStartTime()
    VLab_etime = ReadConfig.getVLabEndTime()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.cp = CreatePracticals(self.driver)

    @pytest.mark.run()
    def test_CreatePracticals(self):
        self.cl.info("************ TestCase: HOD - Creating the Practicals **********")
        self.lp.login(self.username, self.password)
        self.cl.info("************ TestCase: Creating Physical Practical **********")
        self.cp.creatingThePhysicalPractical(self.practical_title, self.practical_description,
                                             self.start_time, self.end_time, self.location)
        self.cl.info("************ TestCase: Creating Virtual Lab **********")
        self.cp.creatingTheVirtualLab(self.VLab_title, self.VLab_description, self.VLab_stime, self.VLab_etime)
