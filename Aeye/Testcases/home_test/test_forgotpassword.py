import time

import pytest

from Aeye.pageObject.home_page.ForgotPasswordPage import ForgotPasswordPage
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Common_Packages.Utility.custom_logger import custom_logger
from Aeye.configuration.read_properties import ReadConfig
from Aeye.pageObject.home_page.LoginPage import LoginPage


@pytest.mark.usefixtures("Aeye_portal_setup")
class TestLogin(metaclass=Logmethodmeta):
    username = ReadConfig.get_username('proctor approver', 'paemail')
    invalidemail = ReadConfig.get_invalid_email('invalid credentials', 'inemail')
    unregisteredemail = ReadConfig.get_unregistered_email('unregistered credentials', 'unregisteredemail')

    @pytest.fixture(autouse=True)
    def classSetup(self, Aeye_portal_setup):
        self.driver = Aeye_portal_setup
        self.lp = LoginPage(self.driver)
        self.sd = SeleniumDriver(self.driver)
        self.cl = custom_logger()
        self.fp = ForgotPasswordPage(self.driver)

    @pytest.mark.order(1)
    def test_forgot_password_page(self):
        self.cl.info("************  Test Case Started : Forgot password page  **********")
        self.lp.forgot_password()
        assert self.lp.forgot_password_page_verify() == "Forgot Password"

    @pytest.mark.order(2)
    def test_invalid_email(self):
        self.test_forgot_password_page()
        self.lp.enterUsername(self.invalidemail)
        assert self.lp.verify_invalid_email() == "Invalid email"

    @pytest.mark.order(3)
    def test_click_reset_password(self):
        self.test_forgot_password_page()
        self.lp.enterUsername(self.username)
        self.fp.click_reset_password_button()
        assert self.fp.verify_forget_password_link_sent() == "Password Reset link sent. Please check your Email"

    @pytest.mark.order(4)
    def test_unregistered_email(self):
        self.test_forgot_password_page()
        self.lp.enterUsername(self.unregisteredemail)
        self.fp.click_reset_password_button()
        assert self.fp.verify_unregistered_email_alert() == "User matching query does not exist."

    @pytest.mark.order(5)
    def test_click_back_to_login_button(self):
        self.test_click_reset_password()
        self.fp.click_back_to_login_button()
        assert self.fp.verify_login_page() == "Login"
