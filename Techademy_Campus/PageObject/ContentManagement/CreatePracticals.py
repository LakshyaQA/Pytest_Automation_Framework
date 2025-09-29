import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class CreatePracticals(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the creating both kind of practicals content for a chapter under a subject

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating both physical lab and virtual lab

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    CreatePractical_content = "//span[text()='Create Practical']"
    PracticalTitle = "//input[@name='title']"
    PracticalDescription = "//textarea[@name='description']"
    ConductedBy = "//div[@name='conductedBy']"
    UserSelection = "//span[text()='hod@campusqa.in']"  # (//input[@type='search'])[1]
    SelectDate = "//input[@placeholder='mm/dd/yyyy']"  # (//input[@type='tel'])[1]
    StartTime = "(//input[@placeholder='hh:mm (a|p)m'])[1]"  # (//input[@type='tel'])[2]
    EndTime = "(//input[@placeholder='hh:mm (a|p)m'])[2]"  # (//input[@type='tel'])[3]
    Location = "//input[@name='location']"
    VirtualLab_radiobutton = "(//input[@name='controlled-radio-buttons-group'])[2]"
    SelectLab = "(//input[@type='search'])[2]"
    VirtualLab_name = "//li[text()='100 JavaScript Algorithm Challenges']"
    EndDate = "(//input[@type='tel'])[4]"
    SubmitButton = "//button[text()='Submit']"

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

    def clickOnCreatePractical(self):
        self.wait_for_element(self.CreatePractical_content, locator_type="xpath")
        self.element_click_js(self.CreatePractical_content, "xpath")

    def clickEnterPhysical_PracticalTitle(self, practical_title):
        self.wait_for_element(self.PracticalTitle, locator_type="xpath")
        self.element_click_js(self.PracticalTitle, "xpath")
        self.send_keys(practical_title, self.PracticalTitle, "xpath")

    def clickEnterPhysical_PracticalDescription(self, practical_description):
        self.wait_for_element(self.PracticalDescription, locator_type="xpath")
        self.element_click_js(self.PracticalDescription, "xpath")
        self.send_keys(practical_description, self.PracticalDescription, "xpath")

    def clickOnVirtualLab(self):
        self.element_click_js(self.VirtualLab_radiobutton, "xpath")

    def clickOnSelectLab(self):
        self.wait_for_element(self.SelectLab, locator_type="xpath")
        self.element_click_js(self.SelectLab, "xpath")

    def selectTheVirtualLab(self):
        self.element_click(self.SelectLab, "xpath")
        self.element_click(self.VirtualLab_name, "xpath")

    def clickEnterVirtualLabTitle(self, VLab_title):
        self.wait_for_element(self.PracticalTitle, locator_type="xpath")
        self.element_click_js(self.PracticalTitle, "xpath")
        self.send_keys(VLab_title, self.PracticalTitle, "xpath")

    def clickEnterVirtualLabDescription(self, VLab_description):
        self.wait_for_element(self.PracticalDescription, locator_type="xpath")
        self.element_click_js(self.PracticalDescription, "xpath")
        self.send_keys(VLab_description, self.PracticalDescription, "xpath")

    def clickOnConductedBy(self):
        self.wait_for_element(self.ConductedBy, locator_type="xpath")
        self.element_click_js(self.ConductedBy, "xpath")

    def selectConductedByUser(self):
        self.element_click(self.ConductedBy, "xpath")
        self.element_click(self.UserSelection, "xpath")

    def clickOnSelectDate(self):
        self.wait_for_element(self.SelectDate, locator_type="xpath")
        self.element_click_js(self.SelectDate, "xpath")
        date = self.get_current_date(0)
        string_date = str(date)
        self.send_keys(string_date, self.SelectDate, locator_type="xpath")

    def clickEnterStartTime(self, start_time):
        self.wait_for_element(self.StartTime, locator_type="xpath")
        self.element_click_js(self.StartTime, "xpath")
        self.send_keys(start_time, self.StartTime, "xpath")

    def clickEnterEndTime(self, end_time):
        self.wait_for_element(self.EndTime, locator_type="xpath")
        self.element_click_js(self.EndTime, "xpath")
        self.send_keys(end_time, self.EndTime, "xpath")

    def clickEnterVLabStartTime(self, VLab_stime):
        self.wait_for_element(self.StartTime, locator_type="xpath")
        self.element_click_js(self.StartTime, "xpath")
        self.send_keys(VLab_stime, self.StartTime, "xpath")

    def clickEnterVLabEndTime(self, VLab_etime):
        self.wait_for_element(self.EndTime, locator_type="xpath")
        self.element_click_js(self.EndTime, "xpath")
        self.send_keys(VLab_etime, self.EndTime, "xpath")

    def clickOnEndDate(self):
        self.wait_for_element(self.EndDate, locator_type="xpath")
        self.element_click_js(self.EndDate, "xpath")
        date = self.get_current_date(2)
        string_date = str(date)
        self.send_keys(string_date, self.EndDate, locator_type="xpath")

    def clickEnterLocation(self, location):
        self.wait_for_element(self.Location, locator_type="xpath")
        self.element_click_js(self.Location, "xpath")
        self.send_keys(location, self.Location, "xpath")

    def clickOnSubmitButton(self):
        self.element_click_js(self.SubmitButton, "xpath")

    def creatingThePhysicalPractical(self, practical_title, practical_description, start_time, end_time,
                                     location):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnCreatePractical()
        self.clickEnterPhysical_PracticalTitle(practical_title)
        self.clickEnterPhysical_PracticalDescription(practical_description)
        self.clickOnConductedBy()
        self.selectConductedByUser()
        self.clickOnSelectDate()
        self.clickEnterStartTime(start_time)
        self.clickEnterEndTime(end_time)
        self.clickEnterLocation(location)
        self.clickOnSubmitButton()
        time.sleep(3)

    def creatingTheVirtualLab(self, VLab_title, VLab_description, VLab_stime, VLab_etime):
        self.clickOnAddContent()
        self.clickOnCreatePractical()
        self.clickEnterVirtualLabTitle(VLab_title)
        self.clickEnterVirtualLabDescription(VLab_description)
        self.clickOnConductedBy()
        self.selectConductedByUser()
        self.clickOnSelectDate()
        self.clickEnterVLabStartTime(VLab_stime)
        self.clickEnterVLabEndTime(VLab_etime)
        self.clickOnVirtualLab()
        self.clickOnSelectLab()
        self.selectTheVirtualLab()
        self.clickOnEndDate()
        self.clickOnSubmitButton()
        time.sleep(2)
