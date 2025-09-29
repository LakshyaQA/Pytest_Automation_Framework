# import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.bulkUploadStudent import BulkUploadStudent

import unittest
import pytest

@pytest.mark.usefixtures("tech_campus_setup")
class BulkUploadTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.bu = BulkUploadStudent(self.driver)

    @pytest.mark.run()
    def test_bulk_upload_student(self):
        self.cl.info("************   TestCase  : Registrar Role : Bulk Upload Student     ************")
        self.lp.login(self.username, self.password)
        self.bu.bulk_upload_student()
        # self.bu.verify_bulk_upload_student()
        # time.sleep(2)
