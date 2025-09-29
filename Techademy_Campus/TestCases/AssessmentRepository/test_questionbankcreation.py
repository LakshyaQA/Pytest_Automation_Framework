import unittest
import pytest

from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.PageObject.Manualtypeaddingquestionbank import Questionbank
from Techademy_Campus.PageObject.Uploadtypequestionbank import Assessment


@pytest.mark.usefixtures("tech_campus_setup")
class QuestionbankTests(unittest.TestCase):
    Faculty_username = ReadConfig.get_Fac_username()
    Faculty_password = ReadConfig.get_Fac_password()
    HOD_username = ReadConfig.get_HOD_username()
    HOD_password = ReadConfig.get_HOD_password()
    question_bank_name = ReadConfig.get_question_bank_name()
    version = ReadConfig.get_version()
    course_code = ReadConfig.get_course_code()
    duration = ReadConfig.get_duration()
    score = ReadConfig.get_score()
    co = ReadConfig.get_mapped_co()
    pi = ReadConfig.get_mapped_pi()
    question_text = ReadConfig.get_question_text()
    option1 = ReadConfig.get_option1()
    answer1 = ReadConfig.get_answer('Assessment repository', 'answer1')
    answer2 = ReadConfig.get_answer('Assessment repository', 'answer2')
    answer3 = ReadConfig.get_answer('Assessment repository', 'answer3')
    answer4 = ReadConfig.get_answer('Assessment repository', 'answer4')
    description = ReadConfig.get_appdescription()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.qb = Questionbank(self.driver)
        self.ar = Assessment(self.driver)

    @pytest.mark.last
    def test_fac_manual_type_adding_questions(self):
        self.cl.info("************   TestCase : Faculty Role Manual type adding questions       ************")
        self.lp.login(self.Faculty_username, self.Faculty_password)
        self.qb.navigate_to_manage_tab()
        self.qb.create_question_bank_fac(self.question_bank_name, self.version, self.course_code, self.duration,
                                         self.score,
                                         self.co, self.pi, self.question_text, self.option1, self.answer1,
                                         self.answer2,
                                         self.answer3, self.answer4)
        self.qb.verify_question_bank_creation()
        self.qb.delete_question_bank()
        self.qb.verify_delete_question_bank()

    '''
                    We need to run this script in chrome by default it opening in firefox but after refreshing the page 
                     it moves to logout page in firefox so its working proper chrome browser.
                      Command: py.test path from Repository Root  --browser chrome
                     '''

    @pytest.mark.last
    def test_hod_manual_type_adding_questions(self):
        self.cl.info("************   TestCase : HOD Role : Manual type adding questions       ************")
        self.lp.login(self.HOD_username, self.HOD_password)
        self.qb.navigate_to_manage_tab()
        self.qb.create_question_bank_hod(self.question_bank_name, self.version, self.course_code, self.duration,
                                         self.score,
                                         self.co, self.pi, self.question_text, self.option1, self.answer1,
                                         self.answer2,
                                         self.answer3, self.answer4)
        self.qb.verify_question_bank_creation()
        self.qb.delete_question_bank()
        self.qb.verify_delete_question_bank()
        self.qb.validate_question_bank(self.description)
        self.qb.verify_validate_question_bank()

    @pytest.mark.last
    def test_fac_upload_type_question_creation(self):
        self.cl.info("************   TestCase : Faculty Role : Upload type adding questions       ************")
        self.lp.login(self.Faculty_username, self.Faculty_password)
        self.ar.navigate_to_manage_tab()
        self.ar.create_question_bank_fac(self.question_bank_name, self.version, self.course_code)
        self.ar.verify_question_bank_creation()
        self.ar.delete_question_bank()
        self.ar.verify_delete_question_bank()

    @pytest.mark.last
    def test_hod_upload_type_question_creation(self):
        self.cl.info("************   TestCase : HOD Role : Upload type adding questions       ************")
        self.lp.login(self.HOD_username, self.HOD_password)
        self.ar.navigate_to_manage_tab()
        self.ar.create_question_bank_hod(self.question_bank_name, self.version, self.course_code)
        self.ar.verify_question_bank_creation()
        self.ar.delete_question_bank()
        self.ar.verify_delete_question_bank()
