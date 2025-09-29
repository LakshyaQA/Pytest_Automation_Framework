import time

import Common_Packages.Utility.custom_logger as cl
from Common_Packages.Base.basepage import Basepage


class UserRoles(Basepage):
    log = cl.custom_logger()

    '''
        This class relates to the User Roles where creating/editing/deleting/searching of the roles have been added in
        the HR role under User Management feature.

        author: Abhilash

        '''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators for creating a user role

    manage_tab = "//button[@id='basic-button']"
    UserManagement_option = "//span[text()='User Management']"
    UserRole_tab = "//button[@id='user-management-tab-1']"
    CreateARole_button = "//button[text()='Create a role']"
    RoleName_textfield = "//input[@name='role_name']"
    RoleDesc_textfield = "//input[@name='role_description']"
    CreateNotification_checkbox = "//input[@name='Notification-create']"
    ViewNotification_checkbox = "//input[@name='Notification-list']"
    EditNotification_checkbox = "//input[@name='Notification-update']"
    DeleteNotification_checkbox = "//input[@name='Notification-delete']"
    CreateUserRole_button = "//button[text()='Create User Role']"
    success_message = "//div[contains(text(), 'role created successfully')]"
    EditUserRole_symbol = "(//button[@type='button'])[17]"
    Update_button = "//button[text() = 'Update']"
    DeleteRole_symbol = "(//button[@type='button'])[14]"
    DeleteRole_button = "//button[text()='Delete']"
    UserRole_searchbar = "//input[@id='search-bar']"

    def clickOnManageTab(self):
        self.wait_for_element(self.manage_tab, locator_type="xpath")
        self.element_click_js(self.manage_tab, "xpath")

    def clickOnUserManagement(self):
        self.wait_for_element(self.UserManagement_option, locator_type="xpath")
        self.element_click_js(self.UserManagement_option, "xpath")

    def clickOnUserRoleTab(self):
        self.wait_for_element(self.UserRole_tab, locator_type="xpath")
        self.element_click_js(self.UserRole_tab, "xpath")

    def clickOnCreateARoleButton(self):
        self.element_click_js(self.CreateARole_button, "xpath")

    def clickOnRoleNameTextfield(self):
        self.wait_for_element(self.RoleName_textfield, locator_type="xpath")
        self.element_click_js(self.RoleName_textfield, "xpath")

    def enterRoleName(self, role_name):
        self.send_keys(role_name, self.RoleName_textfield, "xpath")

    def enterRoleDescription(self, role_desc):
        self.send_keys(role_desc, self.RoleDesc_textfield, "xpath")

    def clickOnRoleDescriptionTextfield(self):
        self.wait_for_element(self.RoleDesc_textfield, locator_type="xpath")
        self.element_click_js(self.RoleDesc_textfield, "xpath")

    def clickOnCreateNotificationCheckbox(self):
        self.element_click_js(self.CreateNotification_checkbox, "xpath")

    def clickOnViewNotificationCheckbox(self):
        self.element_click_js(self.ViewNotification_checkbox, "xpath")

    def clickOnEditNotificationCheckbox(self):
        self.element_click_js(self.EditNotification_checkbox, "xpath")

    def clickOnDeleteNotificationCheckbox(self):
        self.element_click_js(self.DeleteNotification_checkbox, "xpath")

    def clickOnCreateUserRoleButton(self):
        self.element_click_js(self.CreateUserRole_button, "xpath")

    def clickOnEditSymbol(self):
        self.wait_for_element(self.EditUserRole_symbol, locator_type="xpath")
        self.element_click_js(self.EditUserRole_symbol, "xpath")

    def clickOnRoleDescription(self):
        self.wait_for_element(self.RoleDesc_textfield, locator_type="xpath")
        self.element_click_js(self.RoleDesc_textfield, "xpath")

    def editRoleDescription(self, editRDesc):
        self.send_keys(" " + editRDesc, self.RoleDesc_textfield, "xpath")

    def clickOnUpdateButton(self):
        self.element_click_js(self.Update_button, "xpath")

    def clickOnDeleteSymbol(self):
        self.element_click_js(self.DeleteRole_symbol, "xpath")

    def clickOnDeleteButton(self):
        self.element_click_js(self.DeleteRole_button, "xpath")

    def clickOnSearchbar(self):
        self.wait_for_element(self.UserRole_searchbar, locator_type="xpath")
        self.element_click_js(self.UserRole_searchbar, "xpath")

    def enterRoleInSearchbar(self, search_role):
        self.send_keys(search_role, self.UserRole_searchbar, "xpath")

    def clickOnUserManagementOption(self):
        self.clickOnManageTab()
        self.clickOnUserManagement()
        time.sleep(2)

    def createUserRole(self, role_name, role_desc):
        self.clickOnUserRoleTab()
        self.clickOnCreateARoleButton()
        self.clickOnRoleNameTextfield()
        self.enterRoleName(role_name)
        time.sleep(1)
        self.clickOnRoleDescriptionTextfield()
        self.enterRoleDescription(role_desc)
        time.sleep(1)
        self.clickOnCreateNotificationCheckbox()
        self.clickOnViewNotificationCheckbox()
        self.clickOnEditNotificationCheckbox()
        self.clickOnDeleteNotificationCheckbox()
        time.sleep(1)
        self.clickOnCreateUserRoleButton()
        time.sleep(2)

    def editTheUserRole(self, editRDesc):
        self.clickOnEditSymbol()
        self.clickOnRoleDescription()
        self.editRoleDescription(editRDesc)
        self.clickOnUpdateButton()
        time.sleep(2)

    def deleteTheUserRole(self):
        self.clickOnDeleteSymbol()
        self.clickOnDeleteButton()
        time.sleep(2)

    def searchTheUserRole(self, search_role):
        self.enterRoleInSearchbar(search_role)
        time.sleep(2)
