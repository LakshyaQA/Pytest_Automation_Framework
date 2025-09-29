import unittest
import pytest

from Techademy_Campus.PageObject.Externalevaluation import EXTEvaluation
from Techademy_Campus.PageObject.InternalEvaluation import Evaluation
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Common_Packages.Utility.custom_logger import custom_logger


@pytest.mark.usefixtures("tech_campus_setup")
class EvaluationTests(unittest.TestCase):
    Faculty_username = ReadConfig.get_Fac_username()
    Faculty_password = ReadConfig.get_Fac_password()
    HOD_username = ReadConfig.get_HOD_username()
    HOD_password = ReadConfig.get_HOD_password()
    feedback = ReadConfig.get_evaluation_feedback()
    points = ReadConfig.get_evaluation_points()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ev = Evaluation(self.driver)
        self.ex = EXTEvaluation(self.driver)

    @pytest.mark.last
    def test_faculty_internal_evaluation(self):
        self.cl.info("************  TestCase : Faculty Role : Internal Evaluation       ************")
        self.lp.login(self.Faculty_username, self.Faculty_password)
        self.ev.navigate_to_manage_tab()
        self.ev.int_evaluation_fac(self.feedback, self.points)
        self.ev.verify_internal_evaluation()

    @pytest.mark.last
    def test_hod_internal_evaluation(self):
        self.cl.info("*************    TestCase : HOD Role : Internal Evaluation       ************")
        self.lp.login(self.HOD_username, self.HOD_password)
        self.ev.navigate_to_manage_tab()
        self.ev.int_evaluation_hod(self.feedback, self.points)
        self.ev.verify_internal_evaluation()

    @pytest.mark.last
    def test_faculty_external_evaluation(self):
        self.cl.info("************  TestCase : Faculty Role : External Evaluation       ************")
        self.lp.login(self.Faculty_username, self.Faculty_password)
        self.ex.navigate_to_manage_tab()
        self.ex.ext_evaluation_fac(self.feedback, self.points)
        self.ex.verify_external_evaluation()

    @pytest.mark.last
    def test_hod_external_evaluation(self):
        self.cl.info("************  TestCase : HOD Role : External Evaluation       ************")
        self.lp.login(self.HOD_username, self.HOD_password)
        self.ex.navigate_to_manage_tab()
        self.ex.ext_evaluation_hod(self.feedback, self.points)
        self.ex.verify_external_evaluation()

