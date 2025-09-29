import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.feedback import Feedback
import unittest
import pytest


@pytest.mark.usefixtures("tech_campus_setup")
class FeedbackTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')
    faculty_username = ReadConfig.get_login('faculty information', 'faculty_username')
    faculty_password = ReadConfig.get_login('faculty information', 'faculty_password')
    hod_username = ReadConfig.get_login('hod information', 'hod_username')
    hod_password = ReadConfig.get_login('hod information', 'hod_password')
    student_username = ReadConfig.get_login('student information', 'student_username')
    student_password = ReadConfig.get_login('student information', 'student_password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.fb = Feedback(self.driver)

    @pytest.mark.last
    def test_feedback(self):
        self.cl.info("************    TestCase : Registrar Role : FeedBack         **********")
        self.lp.login(self.username, self.password)
        self.fb.search_feedback()



    @pytest.mark.run(1)
    def test_feedback_faculty(self):
        self.cl.info("************    TestCase : Faculty Role : FeedBack         **********")
        self.lp.login(self.faculty_username, self.faculty_password)
        self.fb.search_feedback()

    @pytest.mark.run(2)
    def test_feedback_hod(self):
        self.cl.info("************    TestCase : HOD Role :  FeedBack         **********")
        self.lp.login(self.hod_username, self.hod_password)
        self.fb.search_feedback()

    @pytest.mark.run(3)
    def test_feedback_student(self):
        self.cl.info("************    TestCase : Student Role : FeedBack         **********")
        self.lp.login(self.student_username, self.student_password)
        self.fb.search_feedback()
        time.sleep(1)
        self.fb.feedback_for_course()
        time.sleep(2)
        self.fb.feedback_for_faculty()
        time.sleep(1)
        self.fb.feedback_for_other()
        time.sleep(1)
        self.fb.verify_feedback_output()
