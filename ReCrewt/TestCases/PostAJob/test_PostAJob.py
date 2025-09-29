import time

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Common_Packages.Utility.custom_logger import custom_logger
from Common_Packages.resources.ConfigPath import UploadFile
from ReCrewt.configuration.JsonPathReader import JsonPathReader
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.Job import Job
from ReCrewt.pageObject.JobDetails import JobDetails
from ReCrewt.pageObject.LoginPage import LoginPage
from ReCrewt.pageObject.PostAJob import PostAJob


@pytest.mark.usefixtures("recrewt_setup")
class TestPostAJob():
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
        self.jobdetails = JobDetails(self.driver)

    @pytest.mark.order(5)
    @pytest.mark.parametrize(
        "postajobdata", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), "PostAJob"))
    def test_create_job_post(self, postajobdata):
        job_title, location, description, job_type, department, no_of_position, min_experience, max_experience, education, technical_skills, non_technical_skills, min_compensation, max_copmpensation, other, requested_by, enddate, detail_description=postajobdata
        try:
         self.cl.info("************  Test Case Started : Post A Job : HR Login  **********")
         self.lp.login(self.username, self.password)
         self.cl.info("Loging using credentials Username :" + self.username + " Password : "+self.password)
         self.hp.click_on_jobs()
         self.job.click_post_a_job()
         actual_result = self.pjob.post_a_job_send_approval(job_title, location, description, job_type, department, no_of_position, min_experience, max_experience, education, technical_skills, non_technical_skills, min_compensation, max_copmpensation, other, requested_by, enddate, detail_description)
         self.cl.info("Msg on screen : " + actual_result)
         self.cl.info("************  Post A Job : HR Login : Assertion IS In Progress **********")
         assert actual_result == "Your approval request sent successfully", self.cl.info("Assertion Failed : Details not saved")
         self.cl.info("************  Test Case Ended : Post A Job : HR Login : Assertion Completed **********")

        except Exception as e:
            screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
            self.sd.attach_screenshot_to_allure(screenshot_file)
            raise e


    @pytest.mark.order(7)
    def test_publish_job_post(self):
       try:
        self.cl.info("************  Test Case Started : Publish A Job : HR Login  **********")
        self.lp.login(self.username, self.password)
        self.cl.info("Loging using credentials Username :" + self.username + " Password : " + self.password)
        self.hp.click_on_jobs()
        self.job.click_view_details_approved_job()
        actual_result = self.pjob.publish_job_post()
        self.cl.info("Msg on screen : " + actual_result)
        self.cl.info("************  Publish A Job : HR Login : Assertion IS In Progress **********")
        assert actual_result == "Posted Job Successfully", self.cl.info("Assertion Failed : Details not saved")
        self.cl.info("************  Test Case Ended : Publish A Job : HR Login : Assertion Completed **********")

       except Exception as e:
        screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
        self.sd.attach_screenshot_to_allure(screenshot_file)
        raise e



