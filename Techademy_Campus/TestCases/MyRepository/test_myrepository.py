import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.myRepository import MyRepository

import unittest
import pytest


@pytest.mark.usefixtures("tech_campus_setup")
class MyRepositoryTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')
    faculty_username = ReadConfig.get_login('faculty information', 'faculty_username')
    faculty_password = ReadConfig.get_login('faculty information', 'faculty_password')
    hod_username = ReadConfig.get_login('hod information', 'hod_username')
    hod_password = ReadConfig.get_login('hod information', 'hod_password')
    student_username = ReadConfig.get_login('student information', 'student_username')
    student_password = ReadConfig.get_login('student information', 'student_password')
    hr_username = ReadConfig.get_login('hr information', 'hr_username')
    hr_password = ReadConfig.get_login('hr information', 'hr_password')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.mr = MyRepository(self.driver)

    @pytest.mark.run(1)
    def test_my_repository_registrar(self):
        self.cl.info("************    TestCase : Registrar Role : My Repository    ************")
        self.lp.login(self.username, self.password)
        self.mr.upload_file_in_my_repository()
        time.sleep(3)
        self.mr.edit_file_name()
        time.sleep(2)
        self.mr.search_name()
        time.sleep(2)
        self.mr.share_file()
        time.sleep(1)
        self.mr.delete_file()
        # time.sleep(1)


    @pytest.mark.run(3)
    def test_my_repository_faculty(self):
        self.cl.info("************    TestCase : Faculty Role : My Repository    ************")
        self.lp.login(self.faculty_username, self.faculty_password)
        self.mr.upload_file_in_my_repository()
        time.sleep(3)
        self.mr.edit_file_name()
        time.sleep(2)
        self.mr.search_name()
        time.sleep(2)
        self.mr.share_file()
        time.sleep(1)
        self.mr.delete_file()
        # time.sleep(1)


    @pytest.mark.run(2)
    def test_my_repository_hod(self):
        self.cl.info("************    TestCase : HOD Role : My Repository    ************")
        self.lp.login(self.hod_username, self.hod_password)
        self.mr.upload_file_in_my_repository()
        time.sleep(1)
        self.mr.edit_file_name()
        time.sleep(1)
        self.mr.search_name()
        time.sleep(1)
        self.mr.share_file()
        time.sleep(1)
        self.mr.delete_file()
        # time.sleep(1)

    @pytest.mark.run(4)
    def test_my_repository_student(self):
        self.cl.info("************    TestCase : Student Role : My Repository    ************")
        self.lp.login(self.student_username, self.student_password)
        self.mr.upload_file_in_my_repository()
        time.sleep(3)
        self.mr.edit_file_name()
        time.sleep(2)
        self.mr.search_name()
        time.sleep(2)
        self.mr.share_file()
        time.sleep(1)
        self.mr.delete_file()
        # time.sleep(1)

    @pytest.mark.run()
    def test_my_repository_hr(self):
        self.cl.info("************    TestCase : HR Role : My Repository    ************")
        self.lp.login(self.hr_username, self.hr_password)
        self.mr.upload_file_in_my_repository()
        time.sleep(3)
        self.mr.edit_file_name()
        time.sleep(2)
        self.mr.search_name()
        time.sleep(2)
        self.mr.share_file()
        time.sleep(1)
        self.mr.delete_file()
        # time.sleep(1)


