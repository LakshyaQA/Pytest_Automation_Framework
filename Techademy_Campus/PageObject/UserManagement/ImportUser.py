import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage
from Common_Packages.resources.ConfigPath import UploadFile


class ImportUser(Basepage):
    log = cl.custom_logger()

    '''
        This class includes the importing of users (Bulk Upload of Users) by the HR role under User Management feature.

        author: Abhilash

        '''

    path = UploadFile.file_upload_path('StaffBulk_Upload.xlsx')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for importing users

    manage_tab = "//button[@id='basic-button']"
    UserManagement_option = "//span[text()='User Management']"
    ImportUser_button = "//button[text()='Import user']"
    DropZone_field = "//div[@class='dropzone']"
    StartImport_button = "//button[text()='START IMPORT']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnUserManagement(self):
        self.wait_for_element(self.UserManagement_option, locator_type="xpath")
        self.element_click_js(self.UserManagement_option, "xpath")

    def clickOnImportUserButton(self):
        self.wait_for_element(self.ImportUser_button, locator_type="xpath")
        self.element_click_js(self.ImportUser_button, "xpath")

    def clickOnDragandDrop(self, path):
        self.log.info("Importing the users in bulk")
        self.element_click(self.DropZone_field, "xpath")
        self.upload_file(path, self.DropZone_field, locator_type="xpath")

    def clickOnStartImportButton(self):
        self.element_click(self.StartImport_button, "xpath")

    def clickOnUserManagementOption(self):
        self.clickOnManageTab()
        self.clickOnUserManagement()

    def importTheUsers(self):
        self.clickOnImportUserButton()
        self.clickOnDragandDrop(self.path)
        self.clickOnStartImportButton()
