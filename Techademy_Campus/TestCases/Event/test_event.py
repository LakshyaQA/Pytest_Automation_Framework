import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.event import Event
import unittest
import pytest


@pytest.mark.usefixtures("tech_campus_setup")
class EventTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.ec = Event(self.driver)



    @pytest.mark.last
    def test_event(self):
        self.cl.info("************    TestCase : Registrar Role : Event    **********")
        self.lp.login(self.username, self.password)
        self.ec.create_event()
        time.sleep(3)
        self.ec.update_event()
        time.sleep(3)
        self.ec.delete_event()
        time.sleep(3)
        # self.ec.click_on_cancel_button()
