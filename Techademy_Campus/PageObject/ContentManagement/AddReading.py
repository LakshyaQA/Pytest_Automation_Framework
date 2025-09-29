import logging
import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class AddReading(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the adding of reading content for a chapter under a subject

        author: Abhilash

        '''

    path = UploadFile.file_upload_path('ReadingFile.pdf')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for adding the reading file

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    AddReadings = "//span[text()='Add Readings']"
    ReadingTitle = "(//input[@type='text'])[2]"
    ReadingDropzone = "(//div[@class='dropzone'])[2]"
    Conditions = "(//input[@name='conditions[0].condition'])[2]"
    ReleaseOn = "//li[contains(text(), 'Release On')]"
    ReleaseOnDateTime = "(//input[@placeholder='mm/dd/yyyy hh:mm (a|p)m'])[4]"
    SpecialAccessStart = "(//input[@placeholder='mm/dd/yyyy hh:mm (a|p)m'])[5]"
    SpecialAccessEnd = "(//input[@placeholder='mm/dd/yyyy hh:mm (a|p)m'])[6]"
    SubmitButton = "(//button[text()='Submit'])[2]"

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

    def clickOnAddReadings(self):
        self.wait_for_element(self.AddReadings, locator_type="xpath")
        self.element_click_js(self.AddReadings, "xpath")

    def clickEnterReadingTitle(self, reading_title):
        self.wait_for_element(self.ReadingTitle, locator_type="xpath")
        self.element_click_js(self.ReadingTitle, "xpath")
        self.send_keys(reading_title, self.ReadingTitle, "xpath")

    def uploadReadingFile(self, path):
        self.log.info("Uploading Reading file")
        self.wait_for_element(self.ReadingDropzone, "xpath")
        self.element_click(self.ReadingDropzone, "xpath")
        self.upload_file(path, self.ReadingDropzone, locator_type="xpath")

    def selectCondition(self):
        self.wait_till_element_invisibility(self.Conditions, "xpath")
        self.element_click_js(self.Conditions, "xpath")
        self.wait_for_element(self.ReleaseOn, "xpath")
        self.element_click_js(self.ReleaseOn, "xpath")
        time.sleep(3)

    def clickOnReleaseOnDateTime(self):
        self.element_click_js(self.ReleaseOnDateTime, "xpath")
        date_time = self.get_current_date_and_time(2)
        logging.info(type(date_time))
        string_date_time = str(date_time)
        logging.info(type(string_date_time))
        self.send_keys(string_date_time, self.ReleaseOnDateTime, locator_type="xpath")

    def clickOnSpecialAccessStart(self):
        self.element_click_js(self.SpecialAccessStart, "xpath")
        date_time = self.get_current_date_and_time(0)
        logging.info(type(date_time))
        string_date_time = str(date_time)
        logging.info(type(string_date_time))
        self.send_keys(string_date_time, self.SpecialAccessStart, locator_type="xpath")

    def clickOnSpecialAccessEnd(self):
        self.element_click_js(self.SpecialAccessEnd, "xpath")
        date_time = self.get_current_date_and_time(1)
        logging.info(type(date_time))
        string_date_time = str(date_time)
        logging.info(type(string_date_time))
        self.send_keys(string_date_time, self.SpecialAccessEnd, locator_type="xpath")

    def clickOnSubmitButton(self):
        self.wait_for_element(self.SubmitButton, locator_type="xpath")
        self.element_click(self.SubmitButton, "xpath")

    def addingTheReadingFile(self, reading_title):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnAddReadings()
        self.clickEnterReadingTitle(reading_title)
        self.uploadReadingFile(self.path)
        self.selectCondition()
        self.clickOnReleaseOnDateTime()
        self.clickOnSpecialAccessStart()
        self.clickOnSpecialAccessEnd()
        self.clickOnSubmitButton()
