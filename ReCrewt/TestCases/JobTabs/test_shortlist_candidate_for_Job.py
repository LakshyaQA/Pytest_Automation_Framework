import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.JsonPathReader import JsonPathReader
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.Job import Job
from ReCrewt.pageObject.JobCandidates import JobCandidates
from ReCrewt.pageObject.JobDetails import JobDetails
from ReCrewt.pageObject.LoginPage import LoginPage
from ReCrewt.pageObject.PostAJob import PostAJob


@pytest.mark.usefixtures("recrewt_setup")
class TestShortlistCandidates():
    username = ReadConfig.getUsername('tenant admin', 'tenantusername1')
    password = ReadConfig.getpassword('tenant admin', 'tenantpassword1')

    @pytest.fixture(autouse=True)
    def classSetup(self,recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.job = Job(self.driver)
        self.pjob = PostAJob(self.driver)
        self.cl = custom_logger()
        self.sd = SeleniumDriver(self.driver)
        self.jobcandidate = JobCandidates(self.driver)
        self.jobdetails = JobDetails(self.driver)

    @pytest.mark.order(8)
    @pytest.mark.parametrize(
        "shortlistdata", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), "ShortlistData"))
    def test_shortlist_candidate_for_job(self, shortlistdata):
        try:
         skills, keywords, min_exp, max_exp, location = shortlistdata
         self.cl.info("************  Test Case Started : Tenant Admin : Shortlist candidates  **********")
         self.lp.login(self.username, self.password)
         self.cl.info("Loging using credentials Username :" + self.username + " Password : " + self.password)
         self.hp.click_on_jobs()
         self.job.click_view_details()
         self.job.click_candidate_tab()
         actual_result = self.jobcandidate.shortlist_candidate_for_Job(skills, keywords, min_exp, max_exp, location)
         self.cl.info("Msg on screen : " + actual_result)
         self.cl.info("************ Tenant Admin : Shortlist candidates : Assertion IS In Progress **********")
         assert actual_result == "Chetan", self.cl.info("Assertion Failed : Details not saved")
         self.cl.info("************  Test Case Ended : Tenant Admin : Shortlist candidates : Assertion Completed **********")

        except Exception as e:
         screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
         self.sd.attach_screenshot_to_allure(screenshot_file)
         raise e