import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.CreateExam import CreateExam
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class CreateExamSchedule(unittest.TestCase):
    username = ReadConfig.get_reg_username()
    password = ReadConfig.get_reg_password()
    cluster = ReadConfig.get_cluster_name()
    department = ReadConfig.get_department_name()
    program = ReadConfig.get_program_name()
    title = ReadConfig.getExamTitle()
    s_date = ReadConfig.getExamStartDate()
    e_date = ReadConfig.getExamEndDate()
    result = ReadConfig.getResultPublishOn()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ce = CreateExam(self.driver)

    @pytest.mark.run()
    def test_create_exam(self):
        self.cl.info("*********** TestCase: Registrar - CreateExamSchedule **********")
        self.lp.login(self.username, self.password)
        self.ce.clickOn_Exam()
        self.ce.select_exam_details()
        self.ce.create_exam(self.title, self.s_date, self.e_date, self.result)
