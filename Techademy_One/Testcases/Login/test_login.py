import unittest

import pytest

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_One.configuration.read_properties import ReadConfig
from Techademy_One.pageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_one_setup")
class LoginTests(unittest.TestCase):
    username = ReadConfig.get_username('common info', 'username')
    password = ReadConfig.get_password('common info', 'password')

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_one_setup):
        self.driver = tech_one_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(1)
    def test_verify_valid_Login(self):
        self.cl.info("************  Test Case Started : Portal Login  **********")
        self.lp.login(self.username, self.password)
        self.lp.login_verification()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(45)
    def test_login_with_invalid_username(self):
        self.cl.info("************  Test Case Started : Portal Login  **********")
        self.lp.login("mainnahidungaemail@address.com", "123456")
        self.lp.verify_invalid_username()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.order(46)
    def test_login_with_invalid_pwd(self):
        self.cl.info("************  Test Case Started : Portal Login  **********")
        self.lp.login(self.username, "123456")
        self.lp.verify_invalid_pwd()