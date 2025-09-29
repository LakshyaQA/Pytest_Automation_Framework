import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class LoginPage(Basepage):
    log = cl.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _username_field = "username"
    _password_field = "password"
    _submit_btn = "//button[normalize-space()='Submit']"
    _login_button = "login"
    _realm_dropdown = "//input[@role='combobox']"
    _dropdown_option = "//li[contains(@id,'option-1')]"
    _next_button = "//button[normalize-space()='Next']"
    # _actual_result_element = "//*[@class='MuiTypography-root MuiTypography-h4 css-1rnspsr']"
    _dashboard_heading_interviewer = "//div[contains(text(), 'Candidate Name')]"
    _dashboard_heading = "//h6[@class='MuiTypography-root MuiTypography-h6 css-1f53gjv']"
    _profile = "//div[@class='MuiAvatar-root MuiAvatar-circular css-1qatrb3']"

    def click_username(self):
        self.element_click(self._username_field, locator_type="name")

    def click_password(self):
        self.wait_for_element(self._password_field, locator_type="name")
        self.element_click(self._password_field, locator_type="name")

    def enter_username(self, username):
        self.send_keys(username, self._username_field, locator_type="name")

    def enter_password(self, password):
        self.send_keys(password, self._password_field, locator_type="name")

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="name")

    def click_submit_button(self):
        self.element_click(self._submit_btn, locator_type="xpath")

    def select_realm(self):
        self.select_element(self._realm_dropdown, self._dropdown_option, locator_type="xpath")

    def click_next(self):
        self.element_click(self._next_button, locator_type="xpath")

    def click_profile_icon(self):
        self.wait_for_element(self._profile, locator_type="xpath")
        self.element_click(self._profile, locator_type="xpath")

    def login(self, username, password):
        self.wait_for_element(self._username_field, locator_type="name")
        self.click_username()
        self.enter_username(username)
        self.click_submit_button()
        # dropdown = self.getElement(self._realm_dropdown, locator_type="xpath")
        # if dropdown is not None:  # incase user is in multiple tenants
        #     self.select_realm()
        #     self.log.info("Selected the user from Tenant dropdown")
        #     self.click_next()

        self.log.info("User not selecting from Tenant dropdown")
        self.wait_for_element(self._password_field, locator_type="name")
        self.click_password()
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_page_load()
        self.wait_for_element(self._dashboard_heading, locator_type="xpath")
        self.log.info("Login successfully using credentials : " + username + " " + password)
        return self.get_text(self._dashboard_heading, locator_type="xpath")

    def interviewerLogin(self, interviewer_username, interviewer_password):
        self.wait_for_element(self._username_field, locator_type="xpath")
        self.click_username()
        self.enter_username(interviewer_username)
        self.click_submit_button()
        self.wait_for_element(self._password_field, locator_type="name")
        self.click_password()
        self.enter_password(interviewer_password)
        self.click_login_button()
        # self.wait_for_page_load()
        # self.click_profile_icon()
        self.wait_for_element(self._dashboard_heading_interviewer, locator_type="xpath")
        self.log.info("Login successfully using credentials : " + interviewer_username + " " + interviewer_password)
        return self.get_text(self._dashboard_heading_interviewer, locator_type="xpath")
