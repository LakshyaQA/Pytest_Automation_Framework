

import Common_Packages.Utility.custom_logger as cl

from Common_Packages.Base.basepage import Basepage


class LoginPage(Basepage):
    log = cl.custom_logger()

    '''
            This class includes the details required for the Logging in into the portal as various user roles available  

            author: Abhilash

            '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "//input[@placeholder ='Email']"
    _password_field = "//input[@placeholder ='Password']"
    _signin_button = "//button[@name='login']"
    _login_button = "//button[text()='Login']"
    _actual_result_element = "//img[@class='techademy-logo']"

    def click_on_login_button(self):
        self.wait_for_element(self._login_button, locator_type="xpath")
        self.element_click(self._login_button, locator_type="xpath")

    def enter_username(self, username):
        self.element_click(self._username_field, locator_type="xpath")
        self.send_keys(username, self._username_field, locator_type="xpath")

    def enter_password(self, password):
        self.element_click(self._password_field, locator_type="xpath")
        self.send_keys(password, self._password_field, locator_type="xpath")

    def click_on_signin_button(self):
        self.element_click(self._signin_button, locator_type="xpath")

    def login(self, username, password):
        self.click_on_login_button()
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_signin_button()
        self.log.info(username + " " + " login successfully")
