import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class DiscussionBoard(Basepage):
    log = cl.custom_logger()

    '''
            This class includes the creation of Discussion using the Discussion Board feature available

            author: Abhilash

            '''

    path = UploadFile.file_upload_path('DiscussionFile.jpg')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating a discussion

    manage_tab = "//button[@id='basic-button']"
    DiscussionBoard_option = ("(//span[@class='MuiTypography-root MuiTypography-link basic-menu-item-icon css-2rvg0p'])"
                              "[11]")
    StartDiscussion_button = "//button[text()='Start a discussion']"
    discussion_title = "//input[@name='title']"
    discussion_desc = "//textarea[@name='description']"
    discussion_dropzone = "//div[@class='dropzone']"
    CreatePoll_checkbox = "//input[@name='createAPoll']"
    poll_OptionOne = "//input[@id='outlined-basic']"
    add_PollOption = ("(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-1ouieb2'])"
                      "[2]")
    poll_OptionTwo = "//input[@name='poolingOptions.1.option_text']"
    sendInvitesTo_dropdown = "//input[@type='search']"
    user_option = "//li[text()='student@campusqa.in']"
    submit_button = "//button[text()='Submit']"
    cancel_button = "//button[text()='Cancel']"
    search_by_title = "//input[@placeholder='Search By Title']"
    selecting_date = "//input[@placeholder='mm/dd/yyyy']"
    clear_filter = "//button[text()='Clear filter']"
    up_vote = "(//span[@class='MuiButton-icon MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[1]"
    down_vote = "(//span[@class='MuiButton-icon MuiButton-startIcon MuiButton-iconSizeMedium css-6xugel'])[2]"
    replies = "//li[text()=' Replies']"
    reply_textbox = "//input[@name='comment']"
    add_comment_button = "//button[text()='Add comment']"
    success_message = "//div[text()='Discussion created']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnDiscussionBoard(self):
        self.wait_for_element(self.DiscussionBoard_option, locator_type="xpath")
        self.element_click_js(self.DiscussionBoard_option, locator_type="xpath")

    def clickOnStartDiscussion(self):
        self.element_click_js(self.StartDiscussion_button, locator_type="xpath")

    def clickOnDiscussionTitle(self):
        self.wait_for_element(self.discussion_title, "xpath")
        self.element_click_js(self.discussion_title, "xpath")

    def clickOnDiscussionDescription(self):
        self.wait_for_element(self.discussion_desc, "xpath")
        self.element_click_js(self.discussion_desc, "xpath")

    def clickOnCreatePoll(self):
        self.element_click_js(self.CreatePoll_checkbox, "xpath")

    def clickOnPollOptionOne(self):
        self.element_click_js(self.poll_OptionOne, "xpath")

    def clickOnAddPollOption(self):
        self.element_click_js(self.add_PollOption, "xpath")

    def clickOnPollOptionTwo(self):
        self.element_click_js(self.poll_OptionTwo, "xpath")

    def clickOnSendInvitesTo(self):
        self.wait_for_element(self.sendInvitesTo_dropdown, "xpath")
        self.element_click_js(self.sendInvitesTo_dropdown, "xpath")

    def enterDiscussionTitle(self, title):
        self.send_keys(title, self.discussion_title, "xpath")

    def enterDiscussionDesc(self, desc):
        self.send_keys(desc, self.discussion_desc, "xpath")

    def uploadDiscussionFile(self, path):
        self.log.info("Uploading Discussion File")
        self.element_click(self.discussion_dropzone, "xpath")
        self.upload_file(path, self.discussion_dropzone, locator_type="xpath")

    def enterPollOptionOne(self, poll_one):
        self.send_keys(poll_one, self.poll_OptionOne, "xpath")
        time.sleep(1)

    def enterPollOptionTwo(self, poll_two):
        self.send_keys(poll_two, self.poll_OptionTwo, "xpath")
        time.sleep(1)

    def selectUserOption(self):
        self.element_click(self.sendInvitesTo_dropdown, "xpath")
        self.element_click(self.user_option, locator_type="xpath")
        time.sleep(1)

    def clickOnSubmitButton(self):
        self.element_click_js(self.submit_button, "xpath")

    def clickOnDiscussionBoardOption(self):
        self.clickOnManageTab()
        time.sleep(1)
        self.clickOnDiscussionBoard()
        time.sleep(1)

    def createDiscussion(self, title, desc, poll_one, poll_two):
        self.clickOnStartDiscussion()
        self.clickOnDiscussionTitle()
        self.enterDiscussionTitle(title)
        time.sleep(2)
        self.clickOnDiscussionDescription()
        self.enterDiscussionDesc(desc)
        time.sleep(2)
        self.uploadDiscussionFile(self.path)
        time.sleep(1)
        self.clickOnCreatePoll()
        time.sleep(1)
        self.clickOnPollOptionOne()
        self.enterPollOptionOne(poll_one)
        self.clickOnAddPollOption()
        time.sleep(1)
        self.clickOnPollOptionTwo()
        self.enterPollOptionTwo(poll_two)
        time.sleep(2)
        self.clickOnSendInvitesTo()
        self.selectUserOption()
        self.clickOnSubmitButton()
        time.sleep(3)

    def discussion_creation_verification(self):
        self.wait_for_element(self.success_message, "xpath")
        return self.is_element_displayed(self.success_message, "xpath")
