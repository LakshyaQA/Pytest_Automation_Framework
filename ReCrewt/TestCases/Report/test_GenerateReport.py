import time
import pytest
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.LoginPage import LoginPage
from ReCrewt.pageObject.ReportPage import ReportPage
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from ReCrewt.configuration.JsonPathReader import JsonPathReader


@pytest.mark.usefixtures("recrewt_setup")
class TestReport:
    username = ReadConfig.getUsername('tenant admin', 'tenantusername1')
    password = ReadConfig.getpassword('tenant admin', 'tenantpassword1')

    @pytest.fixture(autouse=True)
    def class_setup(self, recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.sd = SeleniumDriver(self.driver)
        self.cl = custom_logger()
        self.rp = ReportPage(self.driver)

    @pytest.mark.order(10)
    @pytest.mark.parametrize("emailvalue", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), "EmailID"))
    def test_generate_report_candidate(self, emailvalue):
        emailid = emailvalue
        try:
            self.cl.info("************  Test Case Started : Tenant Admin : Candidate Report  **********")
            self.lp.login(self.username, self.password)
            self.cl.info("Loging using credentials Username :" + self.username + " Password : " + self.password)
            self.hp.click_on_reports()
            time.sleep(5)
            actual_result = self.rp.generate_report_candidate(emailid)
            self.cl.info("************ Tenant Admin : Report : Assertion IS In Progress **********")
            assert actual_result == "Reports sent to your email successfully.", self.cl.info(
                "Assertion Failed : Reports not send")
            self.cl.info(
                "************  Test Case Ended : Tenant Admin : Candidate Report : Assertion Completed **********")

        except Exception as e:
            screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
            self.sd.attach_screenshot_to_allure(screenshot_file)
            raise e

    @pytest.mark.order(11)
    @pytest.mark.parametrize("emailvalue", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), "EmailID"))
    def test_generate_report_employees(self, emailvalue):
        emailid = emailvalue
        try:
            self.cl.info("************  Test Case Started : Tenant Admin : Employees Report  **********")
            self.lp.login(self.username, self.password)
            self.cl.info("Loging using credentials Username :" + self.username + " Password : " + self.password)
            self.hp.click_on_reports()
            time.sleep(5)
            actual_result = self.rp.generate_report_employees(emailid)
            self.cl.info("************ Tenant Admin : Report : Assertion IS In Progress **********")
            assert actual_result == "Reports sent to your email successfully.", self.cl.info(
                "Assertion Failed : Reports not send")
            self.cl.info(
                "************  Test Case Ended : Tenant Admin : Employees Report : Assertion Completed **********")

        except Exception as e:
            screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
            self.sd.attach_screenshot_to_allure(screenshot_file)
            raise e

    @pytest.mark.order(12)
    @pytest.mark.parametrize("job_postings",
                             Jsondatareader.get_data_from_json(JsonPathReader.path_json(), "JobPostings"))
    def test_generate_report_job_posting(self, job_postings):
        date_from, date_to, status, email_id = job_postings
        try:
            self.cl.info("************  Test Case Started : Tenant Admin : Job Posting Report  **********")
            self.lp.login(self.username, self.password)
            self.cl.info("Loging using credentials Username :" + self.username + " Password : " + self.password)
            self.hp.click_on_reports()
            time.sleep(5)
            actual_result = self.rp.generate_report_job_postings(date_from, date_to, status, email_id)
            self.cl.info("************ Tenant Admin : Report : Assertion IS In Progress **********")
            assert actual_result == "Reports sent to your email successfully.", self.cl.info(
                "Assertion Failed : Reports not send")
            self.cl.info(
                "************  Test Case Ended : Tenant Admin : Job Posting Report : Assertion Completed **********")

        except Exception as e:
            screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
            self.sd.attach_screenshot_to_allure(screenshot_file)
            raise e
