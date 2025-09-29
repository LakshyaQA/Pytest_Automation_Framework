import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class AddVideoLink(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the adding video link content for a chapter under a subject

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for adding the video link

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    AddVideo = "//span[text()='Add Video']"
    AddVideoTitle = "//input[@name='title']"
    AddVideoLink_radiobutton = "(//input[@name='radio-buttons-group'])[2]"
    AddVideoLink = "//input[@name='mediaFile']"
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

    def clickEnterVideoTitle(self, AddVideo_title):
        self.wait_for_element(self.AddVideoTitle, locator_type="xpath")
        self.element_click_js(self.AddVideoTitle, "xpath")
        self.send_keys(AddVideo_title, self.AddVideoTitle, "xpath")

    def clickOnAddVideoLinkRadiobutton(self):
        self.wait_for_element(self.AddVideoLink_radiobutton, locator_type="xpath")
        self.element_click_js(self.AddVideoLink_radiobutton, "xpath")

    def clickEnterVideoLink(self, AddVideo_link):
        self.wait_for_element(self.AddVideoLink, locator_type="xpath")
        self.element_click_js(self.AddVideoLink, "xpath")
        self.send_keys(AddVideo_link, self.AddVideoLink, "xpath")

    def clickOnUploadButton(self):
        self.wait_for_element(self.UploadButton, locator_type="xpath")
        self.element_click_js(self.UploadButton, "xpath")

    def addingTheVideoLink(self, AddVideo_title, AddVideo_link):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnAddVideo()
        self.clickEnterVideoTitle(AddVideo_title)
        self.clickOnAddVideoLinkRadiobutton()
        self.clickEnterVideoLink(AddVideo_link)
        self.clickOnUploadButton()

