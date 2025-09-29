

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.programTimeTable import ProgramTimeTable

import unittest
import pytest
# import time

@pytest.mark.usefixtures("tech_campus_setup")
class ProgramTimeTableTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')
    faculty_username = ReadConfig.get_login('faculty information', 'faculty_username')
    faculty_password = ReadConfig.get_login('faculty information', 'faculty_password')
    hod_username = ReadConfig.get_login('hod information', 'hod_username')
    hod_password = ReadConfig.get_login('hod information', 'hod_password')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.pt = ProgramTimeTable(self.driver)

    @pytest.mark.last
    def test_program_time_table(self):
        self.cl.info("************     TestCase : Registrar Role : Program Time Table      **********")
        self.lp.login(self.username, self.password)
        self.pt.enter_program_time_table()

    @pytest.mark.run(1)
    def test_program_time_table_faculty(self):
        self.cl.info("************     TestCase : Faculty Role : Program Time Table      **********")
        self.lp.login(self.faculty_username, self.faculty_password)
        self.pt.program_time_table()


    @pytest.mark.run(2)
    def test_program_time_table_hod(self):
        self.cl.info("************     TestCase : HOD Role : Program Time Table      **********")
        self.lp.login(self.hod_username, self.hod_password)
        self.pt.program_time_table()


