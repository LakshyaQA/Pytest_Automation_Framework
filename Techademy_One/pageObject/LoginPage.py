"""
    This page includes locators and functions of Login page

    """
import allure

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig


class LoginPage(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'login_verification')

    def __init__(self, driver):
        super().__init__(driver)
        self.cl = cl.custom_logger()
        self.driver = driver

    # Locators

    _username_field = "username"
    _password_field = "password"
    _submit_btn = "//button[@type='button']"
    _login_button = "login"
    _realm_dropdown = "//input[@role='combobox']"
    _dropdown_option = "//li[contains(@id,'option-1')]"
    _next_button = "//button[normalize-space()='Next']"
    _actual_result_element = "//div[@class='MuiTypography-root MuiTypography-h4 css-1rnspsr']"
    _invalid_email = "//div[@id='notistack-snackbar' and contains(text(),'Invalid username, please contact admin')]"

    def clickUsername(self):
        self.element_click(self._username_field, locator_type="name")

    def clickPassword(self):
        self.element_click(self._password_field, locator_type="name")

    def enterUsername(self, username):
        self.send_keys(username, self._username_field, locator_type="name")

    def enterPassword(self, password):
        self.send_keys(password, self._password_field, locator_type="name")

    def clickLoginButton(self):
        self.element_click(self._login_button, locator_type="name")

    def clickSubmitButton(self):
        self.element_click(self._submit_btn, locator_type="xpath")

    def selectRealm(self):
        self.select_element(self._realm_dropdown, self._dropdown_option, locator_type="xpath")

    def clickNext(self):
        self.element_click(self._next_button, locator_type="xpath")

    def login(self, username, password):
        self.cl.info("**********  Project : Techademy_One  *************")
        self.wait_for_element(self._username_field, locator_type="name")
        self.clickUsername()
        self.enterUsername(username)
        self.clickSubmitButton()
        # dropdown = self.getElement(self._realm_dropdown, locator_type="xpath")
        # if dropdown is not None:  # incase user is in multiple tenants
        #     self.selectRealm()
        #     self.clickNext()

        self.wait_for_element(self._password_field, locator_type="name")
        self.clickPassword()
        self.enterPassword(password)
        self.clickLoginButton()
        self.log.info(username + " " + " logged in successfully")

    def login_verification(self):
        self.verify_by_element_presence(locator=self._actual_result_element, locator_type="xpath",
                                       result_msg="LoginTest")


    def verify_invalid_username(self):
        self.verify_by_element_presence(self._invalid_email,"xpath","invalidLogin")


    def verify_invalid_pwd(self):
        self.verify_by_element_presence("//div[contains(text(),'Invalid username')]","xpath","invalidPassword")