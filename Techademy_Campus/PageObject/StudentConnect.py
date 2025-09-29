import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class StudentConnect(Basepage):
    log = cl.custom_logger()

    '''
            This class includes the creating connection with particular student of the choice.

            author: Abhilash

            '''

    path = UploadFile.file_upload_path('StudentConnectFile.jpg')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for student connect

    manage_tab = "//button[@id='basic-button']"
    student_option = "//span[text()='Student']"
    StudentConnect_button = "//button[text()='Student Connect']"
    Connect_button = "//button[text()='Connect']"
    SearchStudent_field = "//input[@type='search']"
    StudentName = "(//li[@class='MuiAutocomplete-option'])[1]"
    Title_textfield = "//textarea[@name='note']"
    Description_textfield = "//textarea[@name='description']"
    Dropzone_field = "//div[@class='dropzone']"
    Send_button = "//button[text()='Send']"
    success_message = "//a[contains(text(),'Past Connections')]"
    search_bar = "//input[@id='search-bar']"
    delete_symbol = "(//div[@class='MuiGrid-root css-rfnosa'])[1]"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnStudent(self):
        self.wait_for_element(self.student_option, locator_type="xpath")
        self.element_click_js(self.student_option, "xpath")

    def clickOnStudentConnect(self):
        self.wait_for_element(self.StudentConnect_button, locator_type="xpath")
        self.element_click_js(self.StudentConnect_button, "xpath")

    def clickOnConnectButton(self):
        self.wait_for_element(self.Connect_button, locator_type="xpath")
        self.element_click_js(self.Connect_button, "xpath")

    def clickOnSearchStudent(self):
        self.wait_for_element(self.SearchStudent_field, locator_type="xpath")
        self.element_click_js(self.SearchStudent_field, "xpath")

    def clickOnTitle(self):
        self.wait_for_element(self.Title_textfield, locator_type="xpath")
        self.element_click_js(self.Title_textfield, "xpath")

    def clickOnDescription(self):
        self.wait_for_element(self.Description_textfield, locator_type="xpath")
        self.element_click_js(self.Description_textfield, "xpath")

    def selectStudent(self):
        self.element_click(self.SearchStudent_field, "xpath")
        self.element_click(self.StudentName, "xpath")

    #   self.select_element("SearchStudent_field", "StudentName", "xpath")

    def enterTitle(self, title):
        self.send_keys(title, self.Title_textfield, "xpath")

    def enterDescription(self, description):
        self.send_keys(description, self.Description_textfield, "xpath")

    def uploadConnectionFile(self, path):
        self.log.info("Uploading Student Connection file")
        self.element_click(self.Dropzone_field, "xpath")
        self.upload_file(path, self.Dropzone_field, "xpath")

    def clickOnSendButton(self):
        self.element_click_js(self.Send_button, "xpath")

    def clickOnSearchBox(self):
        self.wait_for_element(self.search_bar, locator_type="xpath")
        self.element_click(self.search_bar, "xpath")

    def enterStudentName(self, search_student):
        self.send_keys(search_student, self.search_bar, "xpath")

    def clickOnDeleteSymbol(self):
        self.element_click(self.delete_symbol, "xpath")

    def StudentConnection(self, title, description):
        self.clickOnManageTab()
        time.sleep(1)
        self.clickOnStudent()
        time.sleep(2)
        self.clickOnStudentConnect()
        time.sleep(1.5)
        self.clickOnConnectButton()
        time.sleep(1.5)
        self.clickOnSearchStudent()
        self.selectStudent()
        time.sleep(2)
        self.clickOnTitle()
        self.enterTitle(title)
        time.sleep(1)
        self.clickOnDescription()
        self.enterDescription(description)
        time.sleep(1)
        self.uploadConnectionFile(self.path)
        self.clickOnSendButton()
        time.sleep(2)

    def SearchStudent(self, search_student):
        self.clickOnSearchBox()
        self.enterStudentName(search_student)
        time.sleep(3)

    def DeleteStudentConnection(self):
        self.clickOnDeleteSymbol()
        time.sleep(2)

    def connection_verification(self):
        self.wait_for_element(self.success_message, locator_type="xpath")
        return self.is_element_displayed(self.success_message, locator_type="xpath")
