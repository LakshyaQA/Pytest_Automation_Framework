import unittest

import pytest


from Common_Packages.Utility.custom_logger import custom_logger
from Techademy_Campus.Configuration.readProperties import ReadConfig
from Techademy_Campus.PageObject.ContentManagement.CreateSession import CreateSession
from Techademy_Campus.PageObject.LoginPage import LoginPage


@pytest.mark.usefixtures("tech_campus_setup")
class CreatingSession(unittest.TestCase):
    username = ReadConfig.get_hod_username()
    password = ReadConfig.get_hod_password()
    hyb_session_title = ReadConfig.getHybSessionTitle()
    hyb_session_description = ReadConfig.getHybSessionDescription()
    topic = ReadConfig.getHybSessionTopic()
    hyb_session_stime = ReadConfig.getHybSessionStartTime()
    hyb_session_etime = ReadConfig.getHybSessionEndTime()
    meet_link = ReadConfig.getSessionMeetLink()
    meet_password = ReadConfig.getHybSessionPassword()
    venue = ReadConfig.getSessionVenue()
    onl_session_title = ReadConfig.getOnlSessionTitle()
    onl_session_description = ReadConfig.getOnlSessionDescription()
    onl_session_stime = ReadConfig.getSessionStartTime()
    onl_session_etime = ReadConfig.getSessionEndTime()
    off_session_title = ReadConfig.getOffSessionTitle()
    off_session_description = ReadConfig.getOffSessionDescription()
    off_session_stime = ReadConfig.getOffSessionStartTime()
    off_session_etime = ReadConfig.getOffSessionEndTime()

    @pytest.fixture(autouse=True)
    def classSetup(self, tech_campus_setup):
        self.driver = tech_campus_setup
        self.lp = LoginPage(self.driver)
        self.cl = custom_logger()
        self.cs = CreateSession(self.driver)

    @pytest.mark.run()
    def test_CreateSession(self):
        self.cl.info("************ TestCase: HOD - Creating the Session **********")
        self.lp.login(self.username, self.password)
        self.cl.info("************ TestCase: Creating Online Session **********")
        self.cs.creatingTheOnlineSession(self.onl_session_title, self.onl_session_description, self.topic,
                                         self.onl_session_stime, self.onl_session_etime, self.meet_link,
                                         self.meet_password)
        self.cs.verify_session_creation()
        self.cl.info("************ TestCase: Creating Offline Session **********")
        self.cs.creatingTheOfflineSession(self.off_session_title, self.off_session_description, self.topic,
                                          self.off_session_stime, self.off_session_etime, self.venue)
        self.cs.verify_session_creation()
        self.cl.info("************ TestCase: Creating Hybrid Session **********")
        self.cs.creatingTheHybridSession(self.hyb_session_title, self.hyb_session_description, self.topic,
                                         self.hyb_session_stime, self.hyb_session_etime, self.meet_link,
                                         self.meet_password, self.venue)
        self.cs.verify_session_creation()
