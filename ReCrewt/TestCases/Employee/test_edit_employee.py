import time

import pytest

from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Utility.Jsondatareader import Jsondatareader
from Common_Packages.Utility.custom_logger import custom_logger
from ReCrewt.configuration.readProperties import ReadConfig
from ReCrewt.pageObject.EmployeeTab import EmployeeTab
from ReCrewt.pageObject.HomePage import HomePage
from ReCrewt.pageObject.LoginPage import LoginPage
from ReCrewt.configuration.JsonPathReader import JsonPathReader


@pytest.mark.usefixtures("recrewt_setup")
class TestEditEmployee:
    username = ReadConfig.getUsername('tenant admin', 'tenantusername1')
    password = ReadConfig.getpassword('tenant admin', 'tenantpassword1')

    @pytest.fixture(autouse=True)
    def classSetup(self, recrewt_setup):
        self.driver = recrewt_setup
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.et = EmployeeTab(self.driver)
        self.cl = custom_logger()
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.order(9)
    @pytest.mark.parametrize("employeeDetails", Jsondatareader.get_data_from_json(JsonPathReader.path_json(), array_name="EmployeeDetails"))
    def test_edit_employee(self, employeeDetails):
        location, designation = employeeDetails
        try:
            self.cl.info("************  Test Case Started : Tenant Admin : Add A Candidate  **********")
            self.lp.login(self.username, self.password)
            self.hp.wait_for_page_load()
            self.hp.click_on_emp()
            time.sleep(2)
            self.et.select_interviewer()
            time.sleep(2)
            actual_result = self.et.edit_interviewer_details(location, designation)
            self.cl.info("Message on Screen :" + actual_result)
            self.cl.info("************ Tenant Admin : Edit Employee Details : Assertion IS In Progress **********")
            assert actual_result == "On-Site", self.cl.info("Assertion Failed : Edit failed")
            self.cl.info("************  Test Case Ended : Tenant Admin : Edit Employee Details :  Assertion Completed "
                         "**********")
        except Exception as e:
            screenshot_file = self.sd.screen_shot(self.sd.get_caller_method_name())
            self.sd.attach_screenshot_to_allure(screenshot_file)
            raise e
