import pytest
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.JsonPathReader import JsonPathReader
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.InterviewerPage import InterviewerPage
from ReCrewt.pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("recrewt_setup")
class TestJobApproved:
    iusername = ReadConfig.getUsername('interviewer', 'interviewerusername')
    ipassword = ReadConfig.getpassword('interviewer', 'interviewerpassword')

    @pytest.fixture(autouse=True)
    def classSetup(self, recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.ip = InterviewerPage(self.driver)
        self.cl = custom_logger()
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.order(6)
    @pytest.mark.parametrize("comment", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), array_name="Comment"))
    def test_job_approved(self, comment):
        enterComment = comment
        try:
            self.cl.info("************  Test Case Started : Employee : Job approval request  **********")
            self.lp.login(self.iusername, self.ipassword)
            self.hp.click_on_jobs()
            actual_result = self.ip.job_approve(enterComment)
            self.cl.info("Message on Screen :" + actual_result)
            self.cl.info("************ Employee : Job approval request : Assertion IS In Progress **********")
            assert actual_result == "Your approval has been successfully recorded"
            self.cl.info("Assertion Failed : Job is not approved")
            self.cl.info("************  Test Case Ended : Employee : Job approval request :  Assertion Completed "
                         "**********")

        except Exception as e:
            screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
            self.sd.attach_screenshot_to_allure(screenshot_file)
            raise e
