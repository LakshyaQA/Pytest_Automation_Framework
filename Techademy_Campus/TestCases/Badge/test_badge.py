import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.badge import Badge
import unittest
import pytest


@pytest.mark.usefixtures("tech_campus_setup")
class BadgeTests(unittest.TestCase):
    username = ReadConfig.get_login('registrar information', 'username')
    password = ReadConfig.get_login('registrar information', 'password')


    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.cb = Badge(self.driver)



    @pytest.mark.run(3)
    def test_badge_all_program(self):
        self.cl.info("************    TestCase : Registrar Role :  Badge with all program     **********")
        self.lp.login(self.username, self.password)
        self.cb.creating_badge_for_all_programs()
        time.sleep(3)
        self.cb.search_badge()
        time.sleep(1)
        self.cb.update_badge()
        time.sleep(2)
        self.cb.refresh_page()
        self.cb.delete_badge()
        time.sleep(3)



        '''
         For Perform all functionality in one time we need to run this script
           in chrome by default it opening in firefox but after refreshing the page 
           it moves to logout page in firefox so its working proper chrome browser.
            Command: py.test path from Repository Root  --browser chrome
           '''




    @pytest.mark.run(1)
    def test_badge_with_new_badge(self):
        self.cl.info("************    TestCase : Registrar Role :  Badge With New Badge    **********")
        self.lp.login(self.username, self.password)
        self.cb.creation_of_badge_with_adding_new_badge()
        self.cb.search_badge()
        time.sleep(1)
        self.cb.update_badge()
        time.sleep(2)
        self.cb.refresh_page()
        self.cb.delete_badge()
        time.sleep(3)

    @pytest.mark.run(2)
    def test_badge_with_library(self):
        self.cl.info("************    TestCase : Registrar Role : Badge with library    **********")
        self.lp.login(self.username, self.password)
        self.cb.creating_badge_from_library()
        self.cb.search_badge()
        time.sleep(1)
        self.cb.update_badge()
        time.sleep(2)
        self.cb.refresh_page()
        self.cb.delete_badge()
        time.sleep(3)




