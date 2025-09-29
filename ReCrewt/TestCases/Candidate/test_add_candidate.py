import unittest

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.JsonPathReader import JsonPathReader
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.AddCandidates import AddCandidates
from ReCrewt.pageObject.CandidateTab import Candidates
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("recrewt_setup")
class TestAddCandidate:
    username = ReadConfig.getUsername('tenant admin', 'tenantusername1')
    password = ReadConfig.getpassword('tenant admin', 'tenantpassword1')

    @pytest.fixture(autouse=True)
    def classSetup(self, recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cd = Candidates(self.driver)
        self.ac = AddCandidates(self.driver)
        self.cl = custom_logger()
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.order(3)
    @pytest.mark.parametrize("candidateDetails", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), array_name="CandidateDetails"))
    def test_add_candidate(self, candidateDetails):
        first_name, last_name, gender, dob, location, email, mobile, skills, role, year, month = candidateDetails
        try:
         self.cl.info("************  Test Case Started : Add A Candidate : HR Login  **********")
         self.lp.login(self.username, self.password)
         self.hp.click_on_candidate()
         self.cd.click_on_add_candidate()
         actual_result = self.ac.add_candidate(first_name, last_name, gender, dob, location, email, mobile, skills, role,
                                              year, month)
         self.cl.info("Message on Screen :" + actual_result)
         self.cl.info("************  Add A Candidate : Add A Candidate : Assertion IS In Progress **********")
         assert actual_result == "Candidate Added Successfully", self.cl.info("Assertion Failed : Candidate Not Added")
         self.cl.info("************  Test Case Ended : Add A Candidate : HR Login : Assertion Completed **********")

        except Exception as e:
         screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
         self.sd.attach_screenshot_to_allure(screenshot_file)
         raise e


    @pytest.mark.order(4)
    def test_add_bulk_candidate(self):
        try:
         self.cl.info("************  Test Case Started : Add Bulk Candidate : HR Login  **********")
         self.lp.login(self.username, self.password)
         self.hp.click_on_candidate()
         actual_result = self.cd.add_bulk_upload()
         self.cl.info("Message on Screen :" + actual_result)
         self.cl.info("************  Add A Candidate : Add Bulk Candidate : Assertion IS In Progress **********")
         assert actual_result == "Bulk Uploading Initiated...", self.cl.info("Assertion Failed : Candidate Not Added")
         self.cl.info("************  Test Case Ended : Add Bulk Candidate : HR Login : Assertion Completed **********")

        except Exception as e:
         screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
         self.sd.attach_screenshot_to_allure(screenshot_file)
         raise e
