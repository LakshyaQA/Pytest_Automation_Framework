import logging

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class UploadVideo(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the creating upload video content for a chapter under a subject

        author: Abhilash

        '''
    path = UploadFile.file_upload_path('Video.mp4')
    path_two = UploadFile.file_upload_path('Video.srt')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for uploading the video file

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    AddVideo = "//span[text()='Add Video']"
    UploadVideo_Title = "//input[@name='title']"
    BrowseVideoFile = "(//label[text()='Browse'])[1]"
    BrowseTranscript = "(//label[text()='Browse'])[2]"
    Conditions = "//input[@name='conditions.condition']"
    ReleaseOn = "//li[contains(text(), 'Release On')]"
    ReleaseOnDateTime = "//input[@placeholder='mm/dd/yyyy hh:mm (a|p)m']"
    UploadButton = "//button[contains(text(), 'Upload')]"

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

    def clickOnAddVideo(self):
        self.wait_for_element(self.AddVideo, locator_type="xpath")
        self.element_click_js(self.AddVideo, "xpath")

    def clickEnterVideoTitle(self, UploadVideo_title):
        self.wait_for_element(self.UploadVideo_Title, locator_type="xpath")
        self.element_click_js(self.UploadVideo_Title, "xpath")
        self.send_keys(UploadVideo_title, self.UploadVideo_Title, "xpath")

    def uploadVideoFile(self, path):
        self.log.info("Uploading Video file")
        self.wait_for_element(self.BrowseVideoFile, "xpath")
        self.element_click(self.BrowseVideoFile, "xpath")
        self.upload_file(path, self.BrowseVideoFile, "xpath")

    def uploadVideoTranscript(self, path_two):
        self.log.info("Uploading Video Transcript file")
        self.wait_for_element(self.BrowseTranscript, "xpath")
        self.element_click(self.BrowseTranscript, "xpath")
        self.upload_file(path_two, self.BrowseTranscript, "xpath")

    def selectCondition(self):
        self.wait_till_element_invisibility(self.Conditions, "xpath")
        self.element_click_js(self.Conditions, "xpath")
        self.wait_for_element(self.ReleaseOn, "xpath")
        self.element_click_js(self.ReleaseOn, "xpath")

    def clickOnReleaseOnDateTime(self):
        self.wait_for_element(self.ReleaseOnDateTime, locator_type="xpath")
        self.element_click_js(self.ReleaseOnDateTime, "xpath")
        date_time = self.get_current_date_and_time(2)
        logging.info(type(date_time))
        string_date_time = str(date_time)
        logging.info(type(string_date_time))
        self.send_keys(string_date_time, self.ReleaseOnDateTime, locator_type="xpath")

    def clickOnUploadButton(self):
        self.wait_for_element(self.UploadButton, locator_type="xpath")
        self.element_click_js(self.UploadButton, "xpath")

    def uploadingTheVideo(self, UploadVideo_title):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnAddVideo()
        self.clickEnterVideoTitle(UploadVideo_title)
        self.uploadVideoFile(self.path)
        self.uploadVideoTranscript(self.path_two)
        self.selectCondition()
        self.clickOnReleaseOnDateTime()
        self.clickOnUploadButton()
