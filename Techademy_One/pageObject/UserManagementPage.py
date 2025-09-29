import time

import allure
from selenium.webdriver import Keys

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Techademy_One.configuration.read_properties import ReadConfig

'''
    This page includes locators and functions of user creation and user management page

    '''


class UserManagement(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'user_creation')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _search_user = "//input[@placeholder='Search User']"
    _download_template_button = "//button[normalize-space()='Download Template']"
    _bulk_upload_button = "//button[normalize-space()='Bulk Upload']"
    _add_user_button = "//img[@src='/main/AddUser.svg']"
    _view_user_button = "//*[text()='Onkar Ambure']"
    _remove_user = "//button[normalize-space()='Remove']"
    _edit_user = "//button[normalize-space()='Edit']"
    _all_users_tab = "//button[normalize-space()='All Users']"
    _user_group_tab = "//button[normalize-space()='User Group']"
    # Create User locators
    _user_first_name = "//*[@name='first_name']"
    _user_last_name = "//*[@name='last_name']"
    _user_email = "//*[@name='email']"
    _role_group_dropdown = "//*[@name='group_id']"
    _role_grp_option = "//li[contains(@id,'option-0')]"
    _create_user_button = "//button[normalize-space()='Create User']"
    _Business_unit_dropdown = "//*[@name='business_unit']"
    _bu_option = "//li[contains(@id,'option-0')]"
    _check_box = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    _validate_user_creation = "//*[@id='notistack-snackbar']"

    def searchUser(self, name):
        ele = self.get_element(self._search_user, locator_type="xpath")
        self.wait_for_element(ele)
        ele.click()
        ele.send_keys(name)
        ele.send_keys(Keys.ENTER)

    def downloadTemplate(self):
        self.element_click(self._download_template_button, locator_type="xpath")

    def clickOnAllUsers(self):
        self.element_click_js(self._all_users_tab,"xpath")

    def clickOnUserGroup(self):
        self.element_click_js(self._user_group_tab,"xpath")

    def bulkUpload(self):
        self.element_click(self._bulk_upload_button, locator_type="xpath")

    def clickViewUser(self):
        self.element_click(self._view_user_button, locator_type="xpath")

    def clickAddUser(self):
        self.element_click_js(self._add_user_button, locator_type="xpath")

    def enterFirstName(self, f_name):
        self.send_keys(f_name, self._user_first_name, locator_type="xpath")

    def enterLastName(self, l_name):
        self.send_keys(l_name, self._user_last_name, locator_type="xpath")

    def enterEmail(self, name):
        random_name = self.generate_random_name(name)
        email = random_name+'@automatetest.com'
        self.send_keys(email, self._user_email, locator_type="xpath")
        print(email)

    def selectRole(self):
        self.select_element(self._role_group_dropdown, self._role_grp_option, locator_type="xpath")

    def selectBU(self):
        self.select_element(self._Business_unit_dropdown, self._bu_option, locator_type="xpath")

    def clickOnCreateUser(self):
        self.element_click_js(self._create_user_button, locator_type="xpath")

    def clickOnCheckBox(self):
        self.element_click(self._check_box, "xpath")

    def CreateUser(self, first_name, last_name, email):
        self.clickAddUser()
        self.enterFirstName(first_name)
        self.enterLastName(last_name)
        self.enterEmail(email)
        self.clickOnCheckBox()
        time.sleep(2)
        self.selectRole()
        self.clickOnCreateUser()
        time.sleep(5)

    def VerifyUserCreation(self):
        self.verify_by_comparing_text(locator=self._validate_user_creation, locator_type="xpath",
                                      expected_result=self.expected_result, result_msg="UserCreationTest")


