import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class CreateInteraction(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the creating peer group interaction 

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating a peer group interaction

    manage_tab = "//button[@id='basic-button']"
    Department_option = "//span[text()='Department']"
    ViewDetails_button = "//button[text()='View Details']"
    ChapterClick = "//p[text()='Electric Boiler']"
    AddContent = "//p[text()='Add Content']"
    PeerGroupInteraction = "//span[text()='Peer Group Interaction']"
    StartInteraction_button = "//button[text()='Start Interaction']"
    interaction_title = "//input[@name='title']"
    interaction_desc = "//textarea[@name='description']"
    interaction_dropzone = "//div[@class='dropzone']"
    CreateAPoll_checkbox = "//input[@name='createAPoll']"
    poll_OptionOne = "//input[@id='outlined-basic']"
    add_PollOption = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1ouieb2'])"
                      "[2]")
    poll_OptionTwo = "//input[@name='poolingOptions.1.option_text']"
    sendInvitesTo_dropdown = "//input[@type='search']"
    user_option = "//li[text()='student@campusqa.in']"
    submit_button = "//button[text()='Submit']"

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

    def clickOnPeerGroupInteraction(self):
        self.wait_for_element(self.PeerGroupInteraction, locator_type="xpath")
        self.element_click_js(self.PeerGroupInteraction, locator_type="xpath")

    def clickOnStartInteraction(self):
        self.element_click_js(self.StartInteraction_button, locator_type="xpath")

    def clickOnInteractionTitle(self):
        self.wait_for_element(self.interaction_title, "xpath")
        self.element_click_js(self.interaction_title, "xpath")

    def clickOnInteractionDescription(self):
        self.wait_for_element(self.interaction_desc, "xpath")
        self.element_click_js(self.interaction_desc, "xpath")

    def clickOnCreatePoll(self):
        self.element_click_js(self.CreateAPoll_checkbox, "xpath")

    def clickOnPollOptionOne(self):
        self.element_click_js(self.poll_OptionOne, "xpath")

    def clickOnAddPollOption(self):
        self.element_click_js(self.add_PollOption, "xpath")

    def clickOnPollOptionTwo(self):
        self.element_click_js(self.poll_OptionTwo, "xpath")

    def clickOnSendInvitesTo(self):
        self.wait_for_element(self.sendInvitesTo_dropdown, "xpath")
        self.element_click_js(self.sendInvitesTo_dropdown, "xpath")

    def enterInteractionTitle(self, title):
        self.send_keys(title, self.interaction_title, "xpath")

    def enterInteractionDesc(self, desc):
        self.send_keys(desc, self.interaction_desc, "xpath")

    def uploadInteractionFile(self):
        self.log.info("Uploading Interaction file")
        self.element_click(self.interaction_dropzone, "xpath")
        self.upload_file(UploadFile.file_upload_path('InteractionFile.jpg'), self.interaction_dropzone,
                         locator_type="xpath")

    def enterPollOptionOne(self, pollone):
        self.send_keys(pollone, self.poll_OptionOne, "xpath")

    def enterPollOptionTwo(self, polltwo):
        self.send_keys(polltwo, self.poll_OptionTwo, "xpath")

    def selectUserOption(self):
        self.element_click(self.sendInvitesTo_dropdown, "xpath")
        self.element_click(self.user_option, locator_type="xpath")

    def clickOnSubmitButton(self):
        self.element_click_js(self.submit_button, "xpath")

    def createInteraction(self, title, desc, pollone, polltwo):
        self.clickOnManageTab()
        self.clickOnDepartment()
        self.clickOnViewDetails()
        self.clickOnChapter()
        self.clickOnAddContent()
        self.clickOnPeerGroupInteraction()
        self.clickOnStartInteraction()
        self.clickOnStartInteraction()
        self.clickOnInteractionTitle()
        self.enterInteractionTitle(title)
        self.clickOnInteractionDescription()
        self.enterInteractionDesc(desc)
        self.uploadInteractionFile()
        self.clickOnCreatePoll()
        self.clickOnPollOptionOne()
        self.enterPollOptionOne(pollone)
        self.clickOnAddPollOption()
        self.clickOnPollOptionTwo()
        self.enterPollOptionTwo(polltwo)
        self.clickOnSendInvitesTo()
        self.selectUserOption()
        self.clickOnSubmitButton()
