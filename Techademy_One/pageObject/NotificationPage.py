"""
    This page includes locators and functions on Notification page

    """

import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.Base.selenium_drivers import SeleniumDriver
from Techademy_One.configuration.read_properties import ReadConfig


class Notification(Basepage):
    log = cl.custom_logger()
    expected_result = ReadConfig.get_expected_result('Expected Results', 'notification_creation')
    Notification1 = ReadConfig.get_notification_title('Notification Creation', 'notification_title')
    desc = ReadConfig.get_description('Notification Creation', 'description')
    notification_title = SeleniumDriver.generate_random_name(Notification1)
    description = SeleniumDriver.generate_random_name(desc)

    def __init__(self, driver):
        super().__init__(driver)
        self.cl = cl.custom_logger()
        self.driver = driver

        # locators in notification page

    _notification_title_field = "//*[@name='subject']"
    _enter_description_field = "//*[@name='notification_content']"
    _select_user_dropdown_option = "//li[contains(@id,'option-0')]"
    _select_user_dropdown = "//*[@name='recipients_email_ids']"
    _create_notification = "//button[normalize-space()='Create Notification']"
    _back_btn = "//button[normalize-space()='Back']"
    _notification_created_success = "//div[@id='notistack-snackbar']"

    def enternotificationtitle(self, notification_title):
        self.send_keys(notification_title, self._notification_title_field, locator_type="xpath")

    def enterdescription(self, description):
        self.send_keys(description, self._enter_description_field, locator_type="xpath")

    def select_users(self):
        self.wait_till_element_invisibility("//div[@class='loading']", "xpath")
        self.select_element(self._select_user_dropdown, self._select_user_dropdown_option, "xpath")

    def clickoncreatenotification(self):
        self.element_click(self._create_notification, locator_type="xpath")

    def create_notification(self):
        self.enternotificationtitle(self.notification_title)
        self.enterdescription(self.description)
        self.select_users()
        self.clickoncreatenotification()

    def verify_notification_creation(self):
        self.verify_by_comparing_text(locator=self._notification_created_success, locator_type="xpath",
                                      expected_result=self.expected_result,
                                      result_msg="NotificationTests")
