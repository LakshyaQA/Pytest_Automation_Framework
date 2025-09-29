import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.CreateNotification import CreateNotification
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class NotificationTest(unittest.TestCase):
    username = ReadConfig.get_reg_username()
    password = ReadConfig.get_reg_password()
    name = ReadConfig.get_notificationName()
    desc = ReadConfig.get_notificationDesc()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.cn = CreateNotification(self.driver)

    @pytest.mark.run()
    def test_create_notification(self):
        self.cl.info("********** TestCase - CreateNotification **********")
        self.lp.login(self.username, self.password)
        self.cn.create_notification(self.name, self.desc)
        self.cn.create_notification_verification()
        self.cl.info("Passed")
