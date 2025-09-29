import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class UserGroups(Basepage):
    log = cl.custom_logger()

    '''
        This class relates to the User Groups where creating/editing/deleting of the groups have been added in the HR 
        role under User Management feature.

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating, editing, deleting a user group

    manage_tab = "//button[@id='basic-button']"
    UserManagement_option = "//span[text()='User Management']"
    UserGroup_tab = "//button[@id='user-management-tab-2']"
    CreateUserGroup_button = "//button[text()='Create a group']"
    GroupName_textfield = "//input[@name='group_name']"
    GroupDescription_textfield = "//textarea[@name='group_description']"
    CreateAGroup_button = "//button[@type='submit']"
    success_message = "//div[contains(text(), ‘The operation completed successfully’)]"
    GroupName_Selection = "//span[text()='Group 10F']"
    ThreeDots = "(//button[@id='long-button'])[2]"
    EditOption = "//span[text()='Edit']"
    EditGroup_button = "//button[text()='Edit Group']"
    DeleteOption = "//span[text()='Delete']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnUserManagement(self):
        self.wait_for_element(self.UserManagement_option, locator_type="xpath")
        self.element_click_js(self.UserManagement_option, "xpath")

    def clickOnUserGroupsTab(self):
        self.wait_for_element(self.UserGroup_tab, locator_type="xpath")
        self.element_click_js(self.UserGroup_tab, "xpath")

    def clickOnCreateUserGroupButton(self):
        self.element_click_js(self.CreateUserGroup_button, "xpath")

    def clickOnGroupNameTextfield(self):
        self.wait_for_element(self.GroupName_textfield, locator_type="xpath")
        self.element_click_js(self.GroupName_textfield, "xpath")

    def clickOnGroupDescriptionTextfield(self):
        self.wait_for_element(self.GroupDescription_textfield, locator_type="xpath")
        self.element_click_js(self.GroupDescription_textfield, "xpath")

    def enterGroupName(self, group_name):
        self.send_keys(group_name, self.GroupName_textfield, "xpath")

    def enterGroupDescription(self, group_desc):
        self.send_keys(group_desc, self.GroupDescription_textfield, "xpath")

    def clickOnCreateGroupSubmitButton(self):
        self.element_click(self.CreateAGroup_button, "xpath")

    def clickOnGroupName(self):
        self.element_click_js(self.GroupName_Selection, "xpath")

    def clickOnThreeDots(self):
        self.element_click_js(self.ThreeDots, "xpath")

    def clickOnEditOption(self):
        self.element_click_js(self.EditOption, "xpath")

    def clickOnDescriptionTextfield(self):
        self.wait_for_element(self.GroupDescription_textfield, locator_type="xpath")
        self.element_click_js(self.GroupDescription_textfield, "xpath")

    def editDescription(self, editGDesc):
        self.send_keys(" " + editGDesc, self.GroupDescription_textfield, "xpath")

    def clickOnEditGroupButton(self):
        self.element_click_js(self.EditGroup_button, "xpath")

    def clickOnTheThreeDots(self):
        self.element_click_js(self.ThreeDots, "xpath")

    def clickOnDeleteOption(self):
        self.element_click_js(self.DeleteOption, "xpath")

    def clickOnUserManagementOption(self):
        self.clickOnManageTab()
        self.clickOnUserManagement()

    def createUserGroup(self, group_name, group_desc):
        self.clickOnUserGroupsTab()
        self.clickOnCreateUserGroupButton()
        self.clickOnGroupNameTextfield()
        self.enterGroupName(group_name)
        self.clickOnGroupDescriptionTextfield()
        self.enterGroupDescription(group_desc)
        self.clickOnCreateGroupSubmitButton()

    def editUserGroup(self, editGDesc):
        self.clickOnGroupName()
        self.clickOnThreeDots()
        self.clickOnEditOption()
        self.clickOnDescriptionTextfield()
        self.editDescription(editGDesc)
        self.clickOnEditGroupButton()

    def deleteUserGroup(self):
        self.clickOnTheThreeDots()
        self.clickOnDeleteOption()



