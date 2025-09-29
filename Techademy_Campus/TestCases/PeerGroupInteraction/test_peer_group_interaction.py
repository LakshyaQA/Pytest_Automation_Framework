# import time
import time

from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.LoginPage import LoginPage
from Techademy_Campus.PageObject.peerGroupInteraction import PeerGroupInteraction
import unittest
import pytest

@pytest.mark.usefixtures("tech_campus_setup")
class PeerGroupTests(unittest.TestCase):
    student_username = ReadConfig.get_login('student information', 'student_username')
    student_password = ReadConfig.get_login('student information', 'student_password')




    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.pg = PeerGroupInteraction(self.driver)

    @pytest.mark.last
    def test_peer_group_interaction(self):
        self.cl.info("************   TestCase : Student Role :  Peer Group interaction  **********")
        self.lp.login(self.student_username, self.student_password)
        self.pg.creating_interaction()
        self.pg.verify_create_interaction()
        time.sleep(1)
        self.pg.search_by_title()
        time.sleep(1)
        # self.pg.search_by_date()
        # time.sleep(1)
        self.pg.vote_and_reply()
        # self.pg.verify_edit_interaction()
        self.pg.verify_comment_interaction()
        time.sleep(1)
        self.pg.edit_created_interaction()
        self.pg.verify_edit_interaction()
        time.sleep(1)
        self.pg.delete_created_interaction()
        self.pg.verify_delete_interaction()
        time.sleep(1)
        # self.pg.report_interaction()
        # self.pg.verify_report_interaction()
        # time.sleep(1)



