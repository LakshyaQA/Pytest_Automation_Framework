from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.AddCandidates import AddCandidates
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.LoginPage import LoginPage
from ReCrewt.pageObject.CandidateTab import Candidates
import unittest
import pytest


@pytest.mark.usefixtures("recrewt_setup")
class TestDeleteCandidate(unittest.TestCase):
    username = ReadConfig.getUsername('tenant admin','tenantusername1')
    password = ReadConfig.getpassword('tenant admin','tenantpassword1')

    @pytest.fixture(autouse=True)
    def classSetup(self, recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.cd = Candidates(self.driver)
        self.cl = custom_logger()

    @pytest.mark.order(13)
    def test_delete_candidate(self):
       try:
        self.cl.info("************  Test Case Started : Delete A Candidate : HR Login  **********")
        self.lp.login(self.username, self.password)
        self.hp.click_on_candidate()
        _actual_result = self.cd.delete_candidate()
        self.cl.info("Message on Screen :" + _actual_result)
        self.cl.info("************  Loging : Delete A Candidate : Assertion IS In Progress **********")
        assert _actual_result == "Candidate Deleted Successfully", self.cl.info("Assertion Failed : Candidate Not Deleted")
        self.cl.info("************  Test Case Ended : Delete A Candidate : HR Login : Assertion Completed **********")

       except Exception as e:
           screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
           self.sd.attach_screenshot_to_allure(screenshot_file)
           raise e


    @pytest.mark.order(14)
    def test_delete_bulk_candidates(self):
       try:
        self.cl.info("************  Test Case Started : Delete Bulk Candidate : HR Login  **********")
        self.lp.login(self.username, self.password)
        self.hp.click_on_candidate()
        _actual_result = self.cd.delete_multiple_candidate()
        self.cl.info("Message on Screen :" + _actual_result)
        self.cl.info("************  Loging : Delete Bulk Candidate : Assertion IS In Progress ***********")
        assert _actual_result == "5 candidates deleted successfully.", self.cl.info("Assertion Failed : Candidate Not Deleted")
        self.cl.info("************  Test Case Ended : Delete Bulk Candidate : HR Login : Assertion Completed **********")

       except Exception as e:
        screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
        self.sd.attach_screenshot_to_allure(screenshot_file)
        raise e