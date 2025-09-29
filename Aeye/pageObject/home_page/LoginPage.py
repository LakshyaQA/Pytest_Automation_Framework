import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Aeye.configuration.read_properties import ReadConfig
from Common_Packages.Base.custom_metaclass import Logmethodmeta


class LoginPage(Basepage, metaclass=Logmethodmeta):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'login_verification')

    def __init__(self, driver):
        super().__init__(driver)
        self.cl = cl.custom_logger()
        self.driver = driver

    # Locators

    _username_field = "username"
    _password_field = "password"
    _login_button = "//button[contains(text(),'Login')]"
    _actual_result_element = "ico_settings"
    _invalid_email = "//p[contains(text(),'Invalid email')]"
    _invalid_password = "//p[contains(text(),'Invalid password')]"
    _forgot_password = "//button[contains(text(),'Forgot Password')]"
    _logout_button = "//div[@class='qa-user-logout-button MuiBox-root css-113lela']"

    def enterUsername(self, username):
        self.send_keys(username, self._username_field, locator_type="id")

    def enterPassword(self, password):
        self.send_keys(password, self._password_field, locator_type="id")

    def clickLoginButton(self):
        self.element_click(self._login_button, locator_type="xpath")

    def clickForgotPassword(self):
        self.element_click(self._forgot_password, locator_type="xpath")

    def login(self, username, password):
        self.cl.info("**********  Project : Aeye  *************")
        self.wait_until_visible(self._username_field, locator_type="name")
        self.enterUsername(username)
        self.wait_until_visible(self._password_field, locator_type="name")
        self.enterPassword(password)
        self.wait_until_clickable(self._login_button, locator_type="xpath")
        self.clickLoginButton()
        # self.wait_until_visible(self._actual_result_element, locator_type="xpath")
        # self.login_verification()
        self.log.info(f"{username} logged in successfully")

    def logout(self):
        self.cl.info("**********  Project : Aeye  *************")
        self.logout_click()

    def logout_click(self):
        self.wait_until_clickable(self._logout_button, locator_type="xpath")
        self.element_click(self._logout_button, locator_type="xpath")

    def login_invalid_email(self, invalidemail):
        self.cl.info("**********  Project : Aeye  *************")
        self.wait_until_clickable(self._username_field, locator_type="name")
        self.enterUsername(invalidemail)
        self.verify_invalid_email()

    def login_invalid_password(self, invalidpassword):
        self.cl.info("**********  Project : Aeye  *************")
        self.wait_until_clickable(self._password_field, locator_type="xpath")
        self.enterPassword(invalidpassword)
        self.wait_until_clickable(self._password_field, locator_type="xpath")
        self.clear_input_field(self._password_field, locator_type="id", element=None)
        self.verify_invalid_password()

    def forgot_password(self):
        self.cl.info("**********  Project : Aeye  *************")
        self.clickForgotPassword()

    def forgot_password_page_verify(self):
        return self.get_text("//h1[contains(text(),'Forgot Password')]", locator_type="xpath")

    def login_verification(self):
        return self.verify_by_element_presence(locator=self._actual_result_element, locator_type="id",
                                               result_msg="LoginPage")
    def verify_invalid_login(self):
        return self.get_text("//div[contains(text(),'User not found')]", locator_type="xpath")

    def verify_invalid_email(self):
        return self.get_text("//p[contains(text(),'Invalid email')]", locator_type="xpath")

    def verify_invalid_password(self):
        return self.get_text("//p[contains(text(),'Invalid password')]", locator_type="xpath")

    def verify_logout(self):
        return self.get_text("//div[contains(text(),'Logged out successfully')]", locator_type="xpath")
