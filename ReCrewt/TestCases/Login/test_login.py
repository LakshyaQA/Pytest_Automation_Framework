import unittest

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("recrewt_setup")
class TestLogin(unittest.TestCase):
    username = ReadConfig.getUsername('tenant admin', 'tenantusername1')
    password = ReadConfig.getpassword('tenant admin', 'tenantpassword1')

    iusername = ReadConfig.getUsername('interviewer', 'interviewerusername')
    ipassword = ReadConfig.getpassword('interviewer', 'interviewerpassword')

    @pytest.fixture(autouse=True)
    def classSetup(self, recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.hp = HomePage(self.driver)
        self.sd = SeleniumDriver(self.driver)


    @pytest.mark.order(1)
    def test_hr_login(self):
        try:
         self.cl.info("************  Test Case Started : Loging : HR Login  **********")
         actual_heading = self.lp.login(self.username, self.password)
         self.cl.info("Msg on Screen :" + actual_heading)
         self.cl.info("Loging using credentials Username :" + self.username + " Password : " + self.password)
         self.cl.info("************  Loging : HR Login : Assertion IS In Progress **********")
         assert actual_heading == "Dashboard", self.cl.info("Assertion Failed : Login Unsuccessful")
         self.cl.info("Login Successfully !!!!")
         self.cl.info("************  Test Case Ended : Loging : HR Login : Assertion Completed **********")

        except Exception as e:
         screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
         self.sd.attach_screenshot_to_allure(screenshot_file)
         raise e

    @pytest.mark.order(2)
    def test_interviewer_login(self):
       try:
        self.cl.info("************  Test Case Started : Loging : Interviewer Login  **********")
        actual_heading_interviewer = self.lp.interviewerLogin(self.iusername, self.ipassword)
        self.cl.info("Message on Screen :" + actual_heading_interviewer)
        self.cl.info("Loging using credentials Username :" + self.iusername + " Password : " + self.ipassword)
        self.cl.info("************  Loging : Interviewer Login : Assertion IS In Progress **********")
        assert actual_heading_interviewer == "Candidate Name", self.cl.info("Assertion Failed : Login Unsuccessful")
        self.cl.info("Interviewer Login Successful !!!!")
        self.cl.info("************  Test Case Ended : Loging : HR Login : Assertion Completed **********")

       except Exception as e:
        screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
        self.sd.attach_screenshot_to_allure(screenshot_file)
        raise e
