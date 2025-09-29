import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.UploadVideo import UploadVideo
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class UploadingVideo(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    UploadVideo_title = ReadConfig.getVideoTitle()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.uv = UploadVideo(self.driver)

    @pytest.mark.run()
    def test_UploadVideo(self):
        self.cl.info("********** TestCase: HOD - UploadVideo *********")
        self.lp.login(self.username, self.password)
        self.uv.uploadingTheVideo(self.UploadVideo_title)
