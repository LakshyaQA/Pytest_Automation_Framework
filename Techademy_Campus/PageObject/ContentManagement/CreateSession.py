import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class CreateSession(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the creating a online, offline & hybrid types of sessions for  a chapter under a subject

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating the online, offline & hybrid sessions

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    CreateSession = "//span[text()='Create Session']"
    SessionTitle = "//input[@name='session_title']"
    SessionDescription = "//textarea[@name='session_desc']"
    SelectFaculty = "//input[@type='search']"
    User = "//span[text()='(hod@campusqa.in)']"
    TopicName = "//input[@name='topic_name']"
    SelectDate = "//input[@placeholder='mm/dd/yyyy']"
    StartTime = "(//input[@placeholder='hh:mm (a|p)m'])[1]"
    EndTime = "(//input[@placeholder='hh:mm (a|p)m'])[2]"
    SelectMode = "//input[@name='meet_type']"
    OnlineMode = "//li[contains(text(), 'Online')]"
    OfflineMode = "//li[contains(text(), 'Offline')]"
    HybridMode = "//li[contains(text(), 'Hybrid')]"
    MeetingLink = "//input[@name='meeting_link']"
    Password = "//input[@name='password']"
    Venue = "//input[@name='location']"
    CreateButton = "//button[text()='Create']"
    success_message = "//div[text()='Session created successfully']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnDepartment(self):
        self.wait_for_element(self.Department_option, locator_type="xpath")
        self.element_click_js(self.Department_option, "xpath")

    def clickOnViewDetails(self):
        self.wait_for_element(self.ViewDetails_button, locator_type="xpath")
        self.element_click_js(self.ViewDetails_button, "xpath")

    def clickOnChapter(self):
        self.wait_for_element(self.ChapterClick, locator_type="xpath")
        self.element_click_js(self.ChapterClick, "xpath")

    def clickOnAddContent(self):
        self.wait_for_element(self.AddContent, locator_type="xpath")
        self.element_click_js(self.AddContent, "xpath")

    def clickOnCreateSession(self):
        self.wait_for_element(self.CreateSession, locator_type="xpath")
        self.element_click_js(self.CreateSession, "xpath")

    def clickEnterOnlSessionTitle(self, onl_session_title):
        self.wait_for_element(self.SessionTitle, locator_type="xpath")
        self.element_click_js(self.SessionTitle, "xpath")
        self.send_keys(onl_session_title, self.SessionTitle, "xpath")

    def clickEnterOffSessionTitle(self, off_session_title):
        self.wait_for_element(self.SessionTitle, locator_type="xpath")
        self.element_click_js(self.SessionTitle, "xpath")
        self.send_keys(off_session_title, self.SessionTitle, "xpath")

    def clickEnterHybSessionTitle(self, hyb_session_title):
        self.wait_for_element(self.SessionTitle, locator_type="xpath")
        self.element_click_js(self.SessionTitle, "xpath")
        self.send_keys(hyb_session_title, self.SessionTitle, "xpath")

    def clickEnterOnlSessionDescription(self, onl_session_description):
        self.wait_for_element(self.SessionDescription, locator_type="xpath")
        self.element_click_js(self.SessionDescription, "xpath")
        self.send_keys(onl_session_description, self.SessionDescription, "xpath")

    def clickEnterOffSessionDescription(self, off_session_description):
        self.wait_for_element(self.SessionDescription, locator_type="xpath")
        self.element_click_js(self.SessionDescription, "xpath")
        self.send_keys(off_session_description, self.SessionDescription, "xpath")

    def clickEnterHybSessionDescription(self, hyb_session_description):
        self.wait_for_element(self.SessionDescription, locator_type="xpath")
        self.element_click_js(self.SessionDescription, "xpath")
        self.send_keys(hyb_session_description, self.SessionDescription, "xpath")

    def clickOnSelectFaculty(self):
        self.wait_for_element(self.SelectFaculty, locator_type="xpath")
        self.element_click_js(self.SelectFaculty, "xpath")

    def selectUser(self):
        self.element_click(self.SelectFaculty, "xpath")
        self.element_click(self.User, "xpath")

    def clickOnTopicName(self):
        self.wait_for_element(self.TopicName, locator_type="xpath")
        self.element_click(self.TopicName, "xpath")

    def enterTopicName(self, topic):
        self.send_keys(topic, self.TopicName, "xpath")

    def clickOnSelectDate(self):
        self.wait_for_element(self.SelectDate, locator_type="xpath")
        self.element_click_js(self.SelectDate, "xpath")
        date = self.get_current_date(0)
        string_date = str(date)
        self.send_keys(string_date, self.SelectDate, locator_type="xpath")

    def clickEnterOnlStartTime(self, onl_session_stime):
        self.wait_for_element(self.StartTime, locator_type="xpath")
        self.element_click_js(self.StartTime, "xpath")
        self.send_keys(onl_session_stime, self.StartTime, "xpath")

    def clickEnterOnlEndTime(self, onl_session_etime):
        self.wait_for_element(self.EndTime, locator_type="xpath")
        self.element_click_js(self.EndTime, "xpath")
        self.send_keys(onl_session_etime, self.EndTime, "xpath")

    def clickEnterOffStartTime(self, off_session_stime):
        self.wait_for_element(self.StartTime, locator_type="xpath")
        self.element_click_js(self.StartTime, "xpath")
        self.send_keys(off_session_stime, self.StartTime, "xpath")

    def clickEnterOffEndTime(self, off_session_etime):
        self.wait_for_element(self.EndTime, locator_type="xpath")
        self.element_click_js(self.EndTime, "xpath")
        self.send_keys(off_session_etime, self.EndTime, "xpath")

    def clickEnterHybStartTime(self, hyb_session_stime):
        self.wait_for_element(self.StartTime, locator_type="xpath")
        self.element_click_js(self.StartTime, "xpath")
        self.send_keys(hyb_session_stime, self.StartTime, "xpath")

    def clickEnterHybEndTime(self, hyb_session_etime):
        self.wait_for_element(self.EndTime, locator_type="xpath")
        self.element_click_js(self.EndTime, "xpath")
        self.send_keys(hyb_session_etime, self.EndTime, "xpath")

    def selectOnlineMode(self):
        self.wait_till_element_invisibility(self.SelectMode, "xpath")
        self.element_click_js(self.SelectMode, "xpath")
        self.wait_for_element(self.OnlineMode, "xpath")
        self.element_click_js(self.OnlineMode, "xpath")

    def selectOfflineMode(self):
        self.wait_till_element_invisibility(self.SelectMode, "xpath")
        self.element_click_js(self.SelectMode, "xpath")
        self.wait_for_element(self.OfflineMode, "xpath")
        self.element_click_js(self.OfflineMode, "xpath")

    def selectHybridMode(self):
        self.wait_till_element_invisibility(self.SelectMode, "xpath")
        self.element_click_js(self.SelectMode, "xpath")
        self.wait_for_element(self.HybridMode, "xpath")
        self.element_click_js(self.HybridMode, "xpath")

    def clickOnMeetingLink(self):
        self.wait_for_element(self.MeetingLink, locator_type="xpath")
        self.element_click_js(self.MeetingLink, "xpath")

    def enterMeetingLink(self, meet_link):
        self.send_keys(meet_link, self.MeetingLink, "xpath")

    def clickOnPassword(self):
        self.wait_for_element(self.Password, locator_type="xpath")
        self.element_click_js(self.Password, "xpath")

    def enterPassword(self, meet_password):
        self.send_keys(meet_password, self.Password, "xpath")

    def clickOnVenue(self):
        self.wait_for_element(self.Venue, "xpath")
        self.element_click_js(self.Venue, "xpath")

    def enterVenue(self, venue):
        self.send_keys(venue, self.Venue, "xpath")

    def clickOnCreateButton(self):
        self.element_click_js(self.CreateButton, "xpath")

    def creatingTheOnlineSession(self, onl_session_title, onl_session_description, topic, onl_session_stime,
                                 onl_session_etime, meet_link, meet_password):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnCreateSession()
        self.clickEnterOnlSessionTitle(onl_session_title)
        self.clickEnterOnlSessionDescription(onl_session_description)
        self.clickOnSelectFaculty()
        self.selectUser()
        self.clickOnTopicName()
        self.enterTopicName(topic)
        self.clickOnSelectDate()
        self.clickEnterOnlStartTime(onl_session_stime)
        self.clickEnterOnlEndTime(onl_session_etime)
        self.selectOnlineMode()
        self.clickOnMeetingLink()
        self.enterMeetingLink(meet_link)
        self.clickOnPassword()
        self.enterPassword(meet_password)
        self.clickOnCreateButton()
        time.sleep(3)

    def creatingTheOfflineSession(self, off_session_title, off_session_description, topic, off_session_stime,
                                  off_session_etime, venue):
        self.clickOnAddContent()
        self.clickOnCreateSession()
        self.clickEnterOffSessionTitle(off_session_title)
        self.clickEnterOffSessionDescription(off_session_description)
        self.clickOnSelectFaculty()
        self.selectUser()
        self.clickOnTopicName()
        self.enterTopicName(topic)
        self.clickOnSelectDate()
        self.clickEnterOffStartTime(off_session_stime)
        self.clickEnterOffEndTime(off_session_etime)
        self.selectOfflineMode()
        self.clickOnVenue()
        self.enterVenue(venue)
        self.clickOnCreateButton()
        time.sleep(3)

    def creatingTheHybridSession(self, hyb_session_title, hyb_session_description, topic, hyb_session_stime,
                                 hyb_session_etime, meet_link, meet_password, venue):
        self.clickOnAddContent()
        self.clickOnCreateSession()
        self.clickEnterHybSessionTitle(hyb_session_title)
        self.clickEnterHybSessionDescription(hyb_session_description)
        self.clickOnSelectFaculty()
        self.selectUser()
        self.clickOnTopicName()
        self.enterTopicName(topic)
        self.clickOnSelectDate()
        self.clickEnterHybStartTime(hyb_session_stime)
        self.clickEnterHybEndTime(hyb_session_etime)
        self.selectHybridMode()
        self.clickOnMeetingLink()
        self.enterMeetingLink(meet_link)
        self.clickOnPassword()
        self.enterPassword(meet_password)
        self.clickOnVenue()
        self.enterVenue(venue)
        self.clickOnCreateButton()
        time.sleep(2)

    def verify_session_creation(self):
        self.wait_for_element(self.success_message, "xpath")
        self.is_element_displayed(self.success_message, "xpath")
