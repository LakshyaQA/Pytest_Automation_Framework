import pytest

from Common_Packages.Base.custom_metaclass import Logmethodmeta
from Common_Packages.Utility.custom_logger import custom_logger
from Aeye.configuration.read_properties import ReadConfig
from Aeye.pageObject.home_page.LoginPage import LoginPage


@pytest.fixture(autouse=True)
def classSetup(request, Aeye_portal_setup):
    driver = Aeye_portal_setup
    lp = LoginPage(driver)
    cl = custom_logger()

    test_class = request.cls
    if test_class:
        test_class.driver = driver
        test_class.lp = lp
        test_class.cl = cl


@pytest.mark.usefixtures("Aeye_portal_setup", "classSetup")
class TestLogin(metaclass=Logmethodmeta):
    username = ReadConfig.get_username('proctor approver', 'paemail')
    password = ReadConfig.get_password('proctor approver', 'papassword')
    invalidemail = ReadConfig.get_invalid_email('invalid credentials', 'inemail')
    invalidpassword = ReadConfig.get_invalid_password('invalid credentials', 'inpassword')

    @pytest.mark.order(1)
    def test_verify_valid_Login(self):
        self.cl.info("************  Test Case Started : Portal Login  **********")
        self.lp.login(self.username, self.password)

    @pytest.mark.order(2)
    def test_login_with_invalid_usrname_pwd(self):
        self.cl.info("************  Test Case Started : Portal Login  **********")
        self.lp.login("mainnahidungaemail@address.com", "123456")
        assert self.lp.verify_invalid_login() == "User not found"

    @pytest.mark.order(3)
    def test_login_with_invalid_email(self):
        self.cl.info("************  Test Case Started : Portal Login-Invalid Email  **********")
        self.lp.login_invalid_email(self.invalidemail)
        assert self.lp.verify_invalid_email() == "Invalid email"

    @pytest.mark.order(4)
    def test_login_with_invalid_password(self):
        self.cl.info("************  Test Case Started : Portal Login-Invalid Password  **********")
        self.lp.login_invalid_password(self.invalidpassword)
        assert self.lp.verify_invalid_password() == "Invalid password"

    @pytest.mark.order(5)
    def test_forgot_Password(self):
        self.cl.info("************  Test Case Started : Forgot Password  **********")
        self.lp.forgot_password()
        assert self.lp.forgot_password_page_verify() == "Forgot Password"

    @pytest.mark.order(6)
    def test_verify_Logout(self):
        self.cl.info("************  Test Case Started : Portal Logout  **********")
        self.lp.login(self.username, self.password)
        self.lp.logout()
        assert self.lp.verify_logout() == "Logged out successfully"
