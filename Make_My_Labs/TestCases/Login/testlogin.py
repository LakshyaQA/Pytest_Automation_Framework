import pytest
from Make_My_Labs.TestCases.BaseTest.testbasetest import Basetest


class Testlogin(Basetest):

    @pytest.mark.order(1)
    def test_valid_login(self):
        self.cl.info(
            "************  Test Case Started : test_valid_login  **********")
        login_page_text = self.lp.get_welcome_text_login()
        self.lp.login(self.username, self.password)
        dashboard_page_text = self.db.get_welcome_text_dashboard()
        assert login_page_text != dashboard_page_text, self.cl.info(
            f"Assertion Failed : {login_page_text} and {dashboard_page_text} are matching")
        self.cl.info(
            "Assertion passed: LoginPage_Text,DashBoard_Text are not matching")
        self.cl.info(
            "************  Test Case Ended : test_valid_login  **********")
